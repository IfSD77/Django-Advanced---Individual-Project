from celery import shared_task


@shared_task
def send_welcome_email(user_email, username):
    print(f"✅ [CELERY TASK] Welcome email would be sent to {user_email} for user {username}")
    print(f"   Subject: Welcome to Structural Portfolio UK, {username}!")
    print(f"   Message: Thank you for registering... (simulated)")

    return f"Welcome email simulated for {user_email}"