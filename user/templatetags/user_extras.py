from django import template

register = template.Library()


def filter_task_completed(value):
    return len([item for item in value if item['is_complete']])

def filter_task_running(value):
    return len([item for item in value if not item['is_complete']])

register.filter("filter_task_completed", filter_task_completed)
register.filter("filter_task_running", filter_task_running)