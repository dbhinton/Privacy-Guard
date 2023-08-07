# Privacy Guard

This is a Django application that allows users to log in with their social media accounts.

## Getting Started

1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the dependencies by running the following command:

pip install -r requirements.txt


4. Migrate the database by running the following command:

python manage.py migrate


5. Run the development server by running the following command:

python manage.py runserver

The development server will be running on port 8000. You can access the application at http://localhost:8000.

6. Go to the register page: http://127.0.0.1:8000/privacy_guard/register/ and input info to register for an account

7. When you get redirected to the login page log in with the credentials you just created

8. Log in and click Download or Delete Data

9. Enter your email to download (open in text editor to see JSON) and/or delete your data


Sure, here are my considerations/thought process of the PII encryption/decryption option determination and an action plan for potential data breach events:

## PII encryption/decryption option determination
I decided to use server-side encryption for the Privacy Guard application because it is the most secure option. This means that the encryption keys are never stored on the client side, which makes it more difficult for attackers to access the data. Server-side encryption is also more scalable than client-side encryption, which is important for an application that is expected to have a large number of users.

Action plan for potential data breach events
In the event of a data breach, I will follow these steps to mitigate the damage:

- Identify the scope of the breach: I will work with my team to identify what data was compromised, who was affected, and how the breach occurred.
- Notify the affected individuals: I will notify the affected individuals as soon as possible about the breach. This notification will include information about the data that was compromised, what steps are being taken to protect the data, and what steps the affected individuals can take to protect themselves.
- Investigate the breach: I will work with law enforcement and security experts to investigate the cause of the breach. This investigation will help us to prevent the breach from happening again.
- Take steps to protect the data: I will take steps to protect the data that was compromised. This may involve implementing additional security measures or changing the way the data is stored.
- Monitor for further unauthorized access: I will monitor the system for any signs of further unauthorized access. This may involve using security tools to detect suspicious activity.

By following these steps, I can help to mitigate the damage caused by a data breach and protect the privacy of my users.

Icebox ideas:
 - Add SSO (I commeted out the SSO Code because I couldn't complete it)



Future 

Author
This application was created by David Hinton.