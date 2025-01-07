from behave import given, when, then
from hamcrest import assert_that, equal_to
from blender import Blender

@given('I have "{thing}" and "{detail}"')
def step_given_add_items(context, thing, detail):
    context.blender = Blender()
    context.blender.add(thing, detail)

@when('I process them')
def step_when_process_items(context):
    context.blender.process()

@then('the result should be "{outcome}"')
def step_then_verify_result(context, outcome):
    assert_that(context.blender.result, equal_to(outcome))
