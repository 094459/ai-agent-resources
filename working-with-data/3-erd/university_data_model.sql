-- University Student Data Model

-- Core entities
CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    DateOfBirth DATE,
    Email VARCHAR(100),
    PhoneNumber VARCHAR(100)
);

CREATE TABLE CareerStatus (
    CareerStatusID INT PRIMARY KEY,
    CareerStatusName VARCHAR(100)
);

CREATE TABLE EvaluationType (
    EvaluationTypeID INT PRIMARY KEY,
    EvaluationTypeName VARCHAR(100),
    IsGroupActivity BIT
);

CREATE TABLE CareerLevel (
    CareerLevelID INT PRIMARY KEY,
    CareerLevelName VARCHAR(100)
);

CREATE TABLE Career (
    CareerID INT PRIMARY KEY,
    CareerName VARCHAR(100),
    DurationYears INT,
    RequiredOptativeCourses INT,
    CareerLevelID INT,
    FOREIGN KEY (CareerLevelID) REFERENCES CareerLevel(CareerLevelID)
);

CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    CareerID INT,
    CourseCode VARCHAR(20),
    Year INT,
    Semester INT,
    Optative BIT,
    FOREIGN KEY (CareerID) REFERENCES Career(CareerID)
);

CREATE TABLE Professor (
    ProfessorID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(100)
);

CREATE TABLE Room (
    RoomID INT PRIMARY KEY,
    RoomCode VARCHAR(10),
    RoomName VARCHAR(100),
    RoomCapacity INT,
    Location VARCHAR(100),
    column_6 INT
);

-- Relationship entities
CREATE TABLE CareerEnrollment (
    CareerEnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CareerID INT,
    EnrollmentDate DATE,
    CareerStatusID INT,
    CareerStatusDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CareerID) REFERENCES Career(CareerID),
    FOREIGN KEY (CareerStatusID) REFERENCES CareerStatus(CareerStatusID)
);

CREATE TABLE CourseOccurrence (
    CourseOccurrenceID INT PRIMARY KEY,
    CourseID INT,
    OccurrenceYear INT,
    CourseOccurrenceCode VARCHAR(20),
    ProfessorID INT,
    StartDate DATE,
    EndDate DATE,
    Capacity INT,
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    FOREIGN KEY (ProfessorID) REFERENCES Professor(ProfessorID)
);

CREATE TABLE CourseEnrollment (
    CourseEnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseOccurrenceID INT,
    FinalScore DECIMAL(5,2),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseOccurrenceID) REFERENCES CourseOccurrence(CourseOccurrenceID)
);

CREATE TABLE Schedule (
    ScheduleID INT PRIMARY KEY,
    CourseOccurrenceID INT,
    DayOfWeek CHAR(2),
    StartTime TIME,
    EndTime TIME,
    RoomID INT,
    FOREIGN KEY (CourseOccurrenceID) REFERENCES CourseOccurrence(CourseOccurrenceID),
    FOREIGN KEY (RoomID) REFERENCES Room(RoomID)
);

CREATE TABLE CourseEnrollmentEvaluation (
    CourseEnrollmentEvaluationID INT PRIMARY KEY,
    CourseEnrollmentID INT,
    EvaluationTypeID INT,
    EvaluationDate DATE,
    Score DECIMAL(5,2),
    FOREIGN KEY (CourseEnrollmentID) REFERENCES CourseEnrollment(CourseEnrollmentID),
    FOREIGN KEY (EvaluationTypeID) REFERENCES EvaluationType(EvaluationTypeID)
);

CREATE TABLE ProfessorCourse (
    ProfessorID INT,
    CourseID INT,
    PRIMARY KEY (ProfessorID, CourseID),
    FOREIGN KEY (ProfessorID) REFERENCES Professor(ProfessorID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

CREATE TABLE AssistantProfessor (
    CourseOccurrenceID INT,
    ProfessorID INT,
    PRIMARY KEY (CourseOccurrenceID, ProfessorID),
    FOREIGN KEY (CourseOccurrenceID) REFERENCES CourseOccurrence(CourseOccurrenceID),
    FOREIGN KEY (ProfessorID) REFERENCES Professor(ProfessorID)
);

CREATE TABLE CourseDependency (
    CourseDependencyID INT PRIMARY KEY,
    CourseID INT,
    RequiredCourseID INT,
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    FOREIGN KEY (RequiredCourseID) REFERENCES Course(CourseID)
);
