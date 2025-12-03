#!/usr/bin/env python3
import boto3
import json
import random
import time
from datetime import datetime

def create_log_group(logs_client, group_name):
    try:
        logs_client.create_log_group(logGroupName=group_name)
        print(f"Created log group: {group_name}")
    except logs_client.exceptions.ResourceAlreadyExistsException:
        print(f"Log group {group_name} already exists")

def create_log_stream(logs_client, group_name, stream_name):
    try:
        logs_client.create_log_stream(logGroupName=group_name, logStreamName=stream_name)
        print(f"Created log stream: {stream_name}")
    except logs_client.exceptions.ResourceAlreadyExistsException:
        print(f"Log stream {stream_name} already exists")

def generate_normal_log():
    endpoints = ["/api/users", "/api/orders", "/api/products", "/health", "/login", "/dashboard"]
    methods = ["GET", "POST", "PUT", "DELETE"]
    status_codes = [200, 201, 204, 304]
    
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "level": "INFO",
        "method": random.choice(methods),
        "endpoint": random.choice(endpoints),
        "status_code": random.choice(status_codes),
        "response_time": random.randint(50, 500),
        "user_id": f"user_{random.randint(1000, 9999)}",
        "message": "Request processed successfully"
    }

def generate_error_log():
    error_types = [
        {"level": "ERROR", "status": 500, "msg": "Internal server error - database connection failed"},
        {"level": "ERROR", "status": 404, "msg": "Resource not found"},
        {"level": "WARN", "status": 429, "msg": "Rate limit exceeded"},
        {"level": "ERROR", "status": 401, "msg": "Authentication failed"},
        {"level": "CRITICAL", "status": 503, "msg": "Service unavailable - downstream service timeout"},
        {"level": "ERROR", "status": 400, "msg": "Invalid request payload"},
        {"level": "WARN", "status": 403, "msg": "Access denied - insufficient permissions"}
    ]
    
    error = random.choice(error_types)
    endpoints = ["/api/users", "/api/orders", "/api/products", "/payment", "/login"]
    
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "level": error["level"],
        "method": random.choice(["GET", "POST", "PUT", "DELETE"]),
        "endpoint": random.choice(endpoints),
        "status_code": error["status"],
        "response_time": random.randint(1000, 5000),
        "user_id": f"user_{random.randint(1000, 9999)}",
        "message": error["msg"],
        "error_code": f"ERR_{random.randint(1000, 9999)}"
    }

def main():
    group_name = input("Enter CloudWatch log group name: ")
    region = input("Enter AWS region: ")
    
    logs_client = boto3.client('logs', region_name=region)
    stream_name = f"web-app-{int(time.time())}"
    
    create_log_group(logs_client, group_name)
    create_log_stream(logs_client, group_name, stream_name)
    
    print(f"Generating log events...")
    
    log_events = []
    for i in range(100):
        if random.random() < 0.9:
            log_data = generate_normal_log()
        else:
            log_data = generate_error_log()
        
        log_events.append({
            'timestamp': int(time.time() * 1000),
            'message': json.dumps(log_data)
        })
        
        time.sleep(0.1)
    
    try:
        logs_client.put_log_events(
            logGroupName=group_name,
            logStreamName=stream_name,
            logEvents=log_events
        )
        print(f"Successfully sent {len(log_events)} log events to {group_name}/{stream_name}")
    except Exception as e:
        print(f"Error sending logs: {e}")

if __name__ == "__main__":
    main()
