---
inclusion: manual
---

# Design Patterns — Full Reference

Detailed examples for each pattern. See `design-patterns.md` for the quick selection guide.

---

## Creational Patterns

### Factory Method
Creates objects without specifying exact classes. Use when object creation logic varies by context.

**Python**:

    def create_repository(storage_type: str) -> Repository:
        factories = {
            "dynamodb": DynamoDBRepository,
            "postgres": PostgresRepository,
            "memory": InMemoryRepository,
        }
        factory = factories.get(storage_type)
        if not factory:
            raise ValueError(f"Unknown storage type: {storage_type}")
        return factory()

**TypeScript**:

    function createRepository(storageType: string): Repository {
        const factories: Record<string, () => Repository> = {
            dynamodb: () => new DynamoDBRepository(),
            postgres: () => new PostgresRepository(),
            memory: () => new InMemoryRepository(),
        }
        const factory = factories[storageType]
        if (!factory) throw new Error(`Unknown storage type: ${storageType}`)
        return factory()
    }

### Builder
Constructs complex objects step-by-step. Essential for objects with many optional parameters.

**Python** — prefer `dataclasses` with defaults or Pydantic models over full Builder classes when the object is simple:

    @dataclass
    class ApiResponse:
        status: int
        body: dict
        headers: dict = field(default_factory=dict)
        cache_ttl: int | None = None
        cors_origin: str | None = None

        class Builder:
            def __init__(self, status: int, body: dict):
                self._status = status
                self._body = body
                self._headers: dict = {}
                self._cache_ttl: int | None = None
                self._cors_origin: str | None = None

            def with_cache(self, ttl: int) -> "ApiResponse.Builder":
                self._cache_ttl = ttl
                return self

            def with_cors(self, origin: str) -> "ApiResponse.Builder":
                self._cors_origin = origin
                return self

            def build(self) -> "ApiResponse":
                return ApiResponse(
                    status=self._status, body=self._body,
                    headers=self._headers, cache_ttl=self._cache_ttl,
                    cors_origin=self._cors_origin,
                )

---

## Structural Patterns

### Adapter
Wraps an incompatible interface to make it work with your code. Essential for AWS SDK responses.

**Python**:

    class CognitoUserAdapter:
        @staticmethod
        def to_domain(cognito_response: dict) -> User:
            attrs = {a["Name"]: a["Value"] for a in cognito_response["UserAttributes"]}
            return User(
                id=cognito_response["Username"],
                email=attrs.get("email", ""),
                name=attrs.get("name", ""),
                verified=attrs.get("email_verified") == "true",
            )

### Decorator
Adds behavior dynamically. Python has first-class support via `@decorator` syntax.

**Python**:

    def require_auth(handler):
        @functools.wraps(handler)
        def wrapper(event, context):
            token = event.get("headers", {}).get("Authorization")
            if not token:
                return {"statusCode": 401, "body": "Unauthorized"}
            event["user"] = verify_token(token)
            return handler(event, context)
        return wrapper

    def cache_response(ttl_seconds: int):
        def decorator(handler):
            @functools.wraps(handler)
            def wrapper(event, context):
                response = handler(event, context)
                response.setdefault("headers", {})["Cache-Control"] = f"max-age={ttl_seconds}"
                return response
            return wrapper
        return decorator

    @require_auth
    @cache_response(ttl_seconds=300)
    def get_dashboard(event, context):
        ...

### Facade
Simplified interface to a complex subsystem. Essential for taming AWS SDK complexity.

**Python**:

    class DocumentService:
        """Facade over S3, DynamoDB, and SNS for document operations."""
        def __init__(self, s3: S3Client, table: Table, topic: SNSTopic):
            self._s3 = s3
            self._table = table
            self._topic = topic

        async def publish_document(self, doc: Document) -> str:
            key = f"documents/{doc.id}/{doc.filename}"
            await self._s3.upload(doc.content, key)
            await self._table.put_item(doc.to_record(s3_key=key))
            await self._topic.publish(DocumentPublished(doc_id=doc.id))
            return key

### Proxy (Caching)
Controls access to an object. Useful for lazy loading, access control, or caching.

**TypeScript**:

    class CachedUserRepository implements UserRepository {
        private cache = new Map<string, User>()
        constructor(private readonly delegate: UserRepository) {}

        async getById(id: string): Promise<User> {
            if (this.cache.has(id)) return this.cache.get(id)!
            const user = await this.delegate.getById(id)
            this.cache.set(id, user)
            return user
        }
    }

---

## Behavioral Patterns

### Strategy
Defines interchangeable algorithms. The most useful pattern for our stack.

**Python**:

    from typing import Protocol

    class NotificationStrategy(Protocol):
        async def send(self, recipient: str, message: str) -> None: ...

    class EmailNotification:
        async def send(self, recipient: str, message: str) -> None:
            await ses.send_email(to=recipient, body=message)

    class NotificationService:
        def __init__(self, strategy: NotificationStrategy):
            self._strategy = strategy

        async def notify(self, recipient: str, message: str) -> None:
            await self._strategy.send(recipient, message)

### Command
Encapsulates a request as an object. Enables undo, queuing, and logging.

**Python**:

    @dataclass
    class CreateOrderCommand:
        customer_id: str
        items: list[OrderItem]
        idempotency_key: str

    class CreateOrderHandler:
        async def handle(self, cmd: CreateOrderCommand) -> Result:
            order = Order.create(cmd.customer_id, cmd.items)
            await self.repository.save(order)
            await self.events.publish(OrderCreated(order.id))
            return Result.success(order.id)

### Template Method
Defines the skeleton of an algorithm, letting subclasses override specific steps.

**Python**:

    class BaseLambdaHandler(ABC):
        def handle(self, event: dict, context) -> dict:
            self.validate(event)
            result = self.process(event)
            return self.format_response(result)

        def validate(self, event: dict) -> None:
            pass  # Override to add custom validation

        @abstractmethod
        def process(self, event: dict) -> Any: ...

        def format_response(self, result: Any) -> dict:
            return {"statusCode": 200, "body": json.dumps(result)}

---

## Patterns to Avoid

- **Abstract Factory**: Only if you genuinely have multiple families of related objects. A simple Factory Method almost always suffices.
- **Singleton**: Creates hidden global state, makes testing harder. Only acceptable for Lambda SDK client init (module-level).
- **Bridge**: Usually overkill for serverless. Prefer Strategy.
- **Flyweight**: Rarely needed — prefer right-sizing Lambda memory or using Step Functions.
- **Visitor**: Only for heterogeneous AST/tree structures. CDK aspects use this.
