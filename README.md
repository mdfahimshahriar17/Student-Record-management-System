# Student Record Management System

A simple terminal-based Student Record Management System built using Python and Object-Oriented Programming (OOP).  
This project allows users to manage students and departments with persistent data storage using JSON files.

## Features

Student Management:

- Add new students
- View all students
- Search students by name, email, or roll number
- Remove students by roll number
- Prevent duplicate roll numbers
- Automatically save student records

Department Management:

- Add departments
- View all departments
- Validate departments when adding students

## Object-Oriented Design

This project follows Object-Oriented Programming principles.

Student → Represents a student  
Department → Represents a department  
StudentManager → Manages student records  
DepartmentManager → Manages departments

Each class has a single responsibility.

## Project Structure

STUDENT_PROJECT/  
│  
├── main.py  
├── data/  
│ ├── students.json  
│ └── departments.json  
│  
├── students/  
│ ├── **init**.py  
│ ├── student.py  
│ └── student_manager.py  
│  
└── departments/  
 ├── **init**.py  
 ├── department.py  
 └── department_manager.py

## Data Storage

All data is stored in JSON format.

students.json stores all student records  
departments.json stores all department records

Data is automatically loaded when the program starts and saved when changes are made.

## How to Run

Install Python 3  
Open terminal in the project root folder  
Run the program using:

python main.py

## System Rules

A student cannot be added unless the department exists  
Roll numbers must be unique  
Student name must contain letters  
Email must be valid

## Purpose

This project is built to demonstrate Object-Oriented Programming and file handling using Python.
