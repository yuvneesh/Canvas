from __future__ import annotations
import json
import requests
from dotenv import load_dotenv
import os


load_dotenv()

with open('urls.json') as json_file:
    urls = json.load(json_file)


def active_courses() -> list[int]:
    """Read the vars.json to obtain and return list of current courses"""
    courses = []

    with open('vars.json') as json_file:
        data = json.load(json_file)
        for i in data["current_courses"]:
            courses.append(i)

    return courses


def all_assignments() -> dict:
    """Get all assignments for current courses"""
    courses = active_courses()

    assignments_dict = {}

    for course in courses:
        print(course_name(course))
        assignments_dict.setdefault(course, [])

        this_assignments = request(
            urls["list_assignments"].format(course_id=course))

        for assignment in this_assignments:
            print(f"    {assignment['name']}")
            assignments_dict[course] = assignment['name']

    return assignments_dict


def course_name(course_id) -> str:
    """Return the course name for <course_id>
    """
    courses = request(urls["list_courses"])
    for course in courses:
        if course["id"] == int(course_id):
            return course["name"]


def request(url) -> json:
    """Make a GET request to the given <url> and return the json response"""
    headers = {'Authorization': f'Bearer {os.getenv("CANVAS_TOKEN")}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to fetch data: {response.status_code}')
