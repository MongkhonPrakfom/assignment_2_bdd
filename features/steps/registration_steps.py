from behave import *
from registration_system import RegistrationSystem

system = RegistrationSystem()


@given('the student enters valid registration details')
def step_given_valid_details(context):
    context.name = "Mongkhon"
    context.email = "mongkhon@gmail.com"


@when('the student submits the registration form')
def step_when_submit_form(context):
    context.result = system.register_student(
        context.name,
        context.email
    )


@then('the registration should be successful')
def step_then_success(context):
    assert context.result == "Registration Successful"


@given('the student leaves the email field empty')
def step_given_empty_email(context):
    context.name = "Mongkhon"
    context.email = ""


@then('an error message should be displayed')
def step_then_error(context):
    assert context.result == "Error: Email is required"