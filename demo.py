import openai
import streamlit as st
from streamlit_chat import message

# Setting page title and header
st.set_page_config(page_title="UST Code Security Analyser", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>UST Code Security Analyser</h1>", unsafe_allow_html=True)

# Set org ID and API key
openai.api_key = "API HERE"

content_message = """ You are a cyber chatbot call cyberGPT. You take only input related to code and cybersecurity. If you are asked a non coding or non cyber related question, such as write me a poem, apologize and refuse. 
OWASP Vulnerabilities list includes the following issues.
1. Broken object level authorization
Object level authorization, typically implemented at the code level for user validation, is a control method to restrict access to objects. When authorization at the object level is not properly enforced, it can expose systems. Such a vulnerability was uncovered at Uber by sending API requests including user phone numbers to get access to tokens and manipulating systems.
Attack vectors: Attacks exploit API endpoints by manipulating object IDs that are sent within a request. This issue is unfortunately fairly common in API-based applications when server-side components do not track the full client state but rely more on object IDs.
Security weakness: Authorization and access controls are complex. Even with proper protocols and configurations, developers sometimes forget to use authorization checks before accessing sensitive objects. These states do not play well with automatic testing.
2. Broken authentication
Authentication endpoints are vulnerable to a number of risks, including brute force attacks, credential stuffing, weak encryption keys, and connections to other microservices without requiring authentication.
Attack vectors: Because these endpoints may be accessible to people outside an organization, there are several potential threats. It’s easy to fail to fully protect the entire boundary for authentication or implement the proper security protocols.
Security weakness: OWASP points to two specific issues with endpoint authentication:
	-A lack of protection mechanisms that include extra levels of protection
	-Incorrect implementation of authentication mechanisms or using the wrong mechanism for applications
3. Broken object property level authorization
When accessing an object via an API, users must be validated to ensure they have the authority to access certain object properties. Broken authorization at the object property level can allow unauthorized users to access and change objects.
Attack vectors: Threat actors exploit vulnerable API endpoints to read, change, add, or delete object property values for objects that should not be available to attackers.
Security weakness: Even when developers provide validations for user access to functions and objects, they may not validate if users are allowed to access specific properties within objects.
4. Unrestricted resource consumption
Without restrictions on API requests, attackers sending multiple requests or flooding resources can implement denial of service (DoS) attacks and also cause financial damage for those using pay-per-request billing. Distributed denial of service (DDoS) attacks have grown significantly over the past two years, up as much as 60%.
Attack vectors: APIs can be exploited by sending multiple, concurrent requests to APIs that do not limit interactions.
Security weakness: APIs often do not limit activities such as execution timeouts, maximum allowable memory, the number of operations in client requests, or implementing third-party spending limits. Even with logging, it’s easy for malicious activity to go unnoticed in the early stages.
5. Broken function level authorization
When function level authorization allows users to access administrative endpoints, they can perform sensitive actions.
Attack vectors: Attackers can uncover API flaws because they are more structured and predictable in access methodology, and then they can send legitimate API calls to endpoints that they should not be able to access. In some cases, it can be as simple as guessing the endpoint URL and changing “users” to “admins” in strings.
Security weakness: Modern applications contain plenty of roles, groups, and complex user hierarchies. Users may have different roles for different areas or objects, so it can be challenging to monitor.
6. Server side request forgery
Server side request forgery (SSRF) can happen when an API fetches a remote resource without first validating the URL supplied by users. Servers can be used as proxies to hide malicious activity. Researchers recently found four such instances of SSRF vulnerabilities with Azure API management, which have since been patched.
Attack vectors: Attackers find an API endpoint that receives a universal resource identifier (URI) and force the application to send a request to an unexpected destination — even when destinations are protected via a firewall or VPN.
Security weakness: Application development often includes accessing URIs provided by the client, and server-side data retrieval generally is not logged or monitored.
7. Security misconfiguration
Hardening security for the API stack should be a top priority for developers, but permissions are often improperly, or inconsistently, applied across cloud services. In other cases, security patches and software are out of date. There have been several high-profile instances where companies failed to protect their cloud resources properly, such as the United States Army Intelligence and Security Command, and in that case the unprotected data included some files classified as top secret.
Attack vectors: Threat actors actively search for unpatched flaws and unprotected files or directories, and they attack common endpoints to map systems and gain unauthorized access. Discrepancies in the way requests are handled and processed leave attack vectors open.
Security weakness: Misconfigurations can happen at any level from network to application. Legacy options and unnecessary services can also create additional attack pathways.
8. Lack of protection from automated threats
Cybercriminals and other threat actors are increasingly evolving their tactics, and APIs are prime targets. Automation is cheap and widely available on the dark web. The APIs themselves may not have flaws or bugs, but the underlying business flow may be vulnerable to excessive activity.
Attack vectors: Attackers learn API models and business flows and then exploit them using automated tools. For example, the use of automated tools and botnets can bypass rate limiting by spreading requests over IP addresses.
Security weakness: The challenge here is that each request may appear legitimate, so it will not be identified as an attack. However, these automated attacks can flood systems and prevent legitimate users from access.
9. Improper inventory management
APIs across applications can be quite complex and interwoven. Connectivity with third parties increase threat exposure, and often multiple versions of APIs may be left running that are unmanaged. Outdated or missing documentation can make it challenging to keep track of everything.
Attack vectors: Attackers may access older API versions or endpoints that are unpatched. They may also gain access through third parties.
Security weakness: A lack of inventory or asset management can lead to a host of problems, including unpatched systems. API hosts may be exposed through microservices, which make applications independent in many cases. A lack of a systematic and documented way to deploy, manage, and retire APIs can lead to different security weaknesses.
10. Unsafe consumption of APIs
When working with well-known third parties and suppliers, you can generally trust the data you receive and might employ less stringent security standards. Yet, if threat actors can breach third parties, they may be able to cause damage through APIs that connect you. Today, as many as half of data breaches occur because of third-party connectivity.
Attack vectors: The exploitation of security flaws in APIs occurs when developers trust — but do not verify and fully protect — endpoints that interact with APIs. For example, they may not place appropriate limitations on resources, validate redirects, or validate/sanitize data requests from APIs before processing.
Security weakness: Security weaknesses often arise when weaker security models are applied to API integrations, especially in areas such as transport security, input validation, data validation, authentication, and authorization. This exposes organizations to unauthorized access and malicious injections.
In addition these are more vulnerabilities:
A01 Broken Access Control moves up from the fifth position; 94% of applications were tested for some form of broken access control. The 34 Common Weakness Enumerations (CWEs) mapped to Broken Access Control had more occurrences in applications than any other category.
A02 Cryptographic Failures shifts up one position to #2, previously known as Sensitive Data Exposure, which was broad symptom rather than a root cause. The renewed focus here is on failures related to cryptography which often leads to sensitive data exposure or system compromise.
A03 Injection slides down to the third position. 94% of the applications were tested for some form of injection, and the 33 CWEs mapped into this category have the second most occurrences in applications. Cross-site Scripting is now part of this category in this edition.
A04 Insecure Design is a new category for 2021, with a focus on risks related to design flaws. If we genuinely want to “move left” as an industry, it calls for more use of threat modeling, secure design patterns and principles, and reference architectures.
A05 Security Misconfiguration moves up from #6 in the previous edition; 90% of applications were tested for some form of misconfiguration. With more shifts into highly configurable software, it’s not surprising to see this category move up. The former category for XML External Entities (XXE) is now part of this category.
A06 Vulnerable and Outdated Components was previously titled Using Components with Known Vulnerabilities and is #2 in the Top 10 community survey, but also had enough data to make the Top 10 via data analysis. This category moves up from #9 in 2017 and is a known issue that we struggle to test and assess risk. It is the only category not to have any Common Vulnerability and Exposures (CVEs) mapped to the included CWEs, so a default exploit and impact weights of 5.0 are factored into their scores.
A07 Identification and Authentication Failures was previously Broken Authentication and is sliding down from the second position, and now includes CWEs that are more related to identification failures. This category is still an integral part of the Top 10, but the increased availability of standardized frameworks seems to be helping.
A08 Software and Data Integrity Failures is a new category for 2021, focusing on making assumptions related to software updates, critical data, and CI/CD pipelines without verifying integrity. One of the highest weighted impacts from Common Vulnerability and Exposures/Common Vulnerability Scoring System (CVE/CVSS) data mapped to the 10 CWEs in this category. Insecure Deserialization from 2017 is now a part of this larger category.
A09 Security Logging and Monitoring Failures was previously Insufficient Logging & Monitoring and is added from the industry survey (#3), moving up from #10 previously. This category is expanded to include more types of failures, is challenging to test for, and isn’t well represented in the CVE/CVSS data. However, failures in this category can directly impact visibility, incident alerting, and forensics.
A10 Server-Side Request Forgery is added from the Top 10 community survey (#1). The data shows a relatively low incidence rate with above average testing coverage, along with above-average ratings for Exploit and Impact potential. This category represents the scenario where the security community members are telling us this is important, even though it’s not illustrated in the data at this time.
Given a program, provide the details of the vulnerabvility and the corresponding fixes. For example,  buffer overrun attack in C++ looks like this:
#include <iostream>
#include <cstring>
using namespace std;
int main() {
   char buffer1[5] = "Hello";
   char buffer2[5];
   // Copy buffer1 to buffer2
   strcpy(buffer2, buffer1);
   cout << "Buffer2: " << buffer2 << endl;
   return 0;
}
while the fixed version looks like 
#include <iostream>
#include <cstring>
using namespace std;
int main() {
   char buffer1[5] = "Hello";
   char buffer2[5];
   // Copy buffer1 to buffer2 with bounds checking
   strncpy(buffer2, buffer1, sizeof(buffer2));
   cout << "Buffer2: " << buffer2 << endl;
   return 0;
}
In this fixed program, strncpy function is used instead of strcpy. strncpy copies the string from buffer1 to buffer2, but it also performs bounds checking by checking the size of the destination buffer buffer2 before copying the data. By using strncpy with bounds checking, we prevent buffer overflow attacks by ensuring that the data being copied is not larger than the destination buffer.
Given the following program 
1. What are the potential vulnerabilities, if any (explain). Name the vulnerability as a title.
2. What are the fixes (with code comments).  Make sure to add code comments in the fixed code. 
"""


# Create a dictionary for OWASP Top 10 Vulnerabilities
owasp_top_10_vulns = {"Broken Access":"""OWASP (Open Web Application Security Project) Broken Access Control is a security vulnerability that occurs when a web application does not properly restrict user access to resources or functionality. This means that users can access resources or perform actions that they should not have permission to do, leading to a potential compromise of the application's security.

Examples of Broken Access Control vulnerabilities include:

1. Unrestricted URL access: A web application may allow a user to access pages or functions without proper authentication or authorization, such as accessing a page that should only be available to an administrator.

2. Direct object references: A web application may use object references, such as IDs, to identify specific resources or functionality. If these references are not properly secured, an attacker may be able to manipulate the references to access resources or functionality that they should not have access to.

3. Insufficient access controls: A web application may not properly restrict access to functionality based on the user's role or permissions, allowing users to perform actions they should not be able to.

4. Session management flaws: A web application may not properly manage user sessions, allowing an attacker to hijack a valid session and gain access to restricted functionality.


To fix Broken Access Control vulnerabilities, it is important to implement proper access controls, such as:

1. Authentication and Authorization: Implement strong authentication and authorization mechanisms to ensure that users are properly authenticated and authorized to access resources and functionality.

2. Proper use of object references: Use proper security measures, such as obfuscation or encryption, to protect object references and prevent manipulation by attackers.

3. Role-based access controls: Implement role-based access controls to ensure that users only have access to functionality that is appropriate for their role or permissions.

4. Secure session management: Implement secure session management techniques, such as session timeouts, to prevent session hijacking and other attacks.


Here is an example of code that has a Broken Access Control vulnerability:

```python
@app.route('/admin')
def admin():
    if not current_user.is_authenticated:
        return redirect('/login')
    if not current_user.is_admin:
        return "Access denied"
    return "Welcome Admin"
```

In this code, the `/admin` route is only accessible to users who are authenticated and have an `is_admin` property set to `True`. However, the code does not verify if the user accessing the route is authorized to do so. An attacker could manipulate the `is_admin` property to gain access to the `admin` route.

To fix this vulnerability, the code should check if the user is authorized to access the `admin` route before granting access:
 

```python
@app.route('/admin')
def admin():
    if not current_user.is_authenticated:
        return redirect('/login')
    if current_user.role != 'admin':
        return "Access denied"
    return "Welcome Admin"
```


In this updated code, the `role` property is used to determine if the user is authorized to access the `admin` route. The code checks if the user's `role` is set to `admin` before granting access. This ensures that only users with the appropriate role can access the `admin` route, preventing Broken Access Control vulnerabilities.""",
                "Control Cryptographic Failures":"""Cryptographic failures can happen in many different ways, such as using weak encryption algorithms, 
poorly designed key management systems, or incorrect implementation of cryptographic functions. Here's an example of a common cryptographic

 
Here is an example of code that is vulnerable to cryptographic failure:

```python
import hashlib

def hash_password(password):
    salt = "random_salt"
    hashed_password = hashlib.sha256(password + salt).hexdigest()
    return hashed_password

password = "mypassword"
hashed_password = hash_password(password)
print(hashed_password)
```

This code is vulnerable to a cryptographic attack because it uses a weak salt value, which can be easily guessed by an attacker. Additionally, it uses a weak hash function (SHA-256) which can be easily brute-forced by an attacker.

To fix this code, we can use a stronger salt value and a more secure hash function. Here is an example of fixed code:

```python
import hashlib
import os

def hash_password(password):
    salt = os.urandom(16)
    hashed_password = hashlib.scrypt(password.encode('utf-8'), salt=salt, n=16384, r=8, p=1)
    return hashed_password.hex()

password = "mypassword"
hashed_password = hash_password(password)
print(hashed_password)
```

In the fixed code, we have used a stronger salt value generated using the os.urandom() method. Additionally, we have used a more secure hash function (scrypt) which is designed to be more resistant to brute-force attacks. We have also used an appropriate number of iterations, memory factor, and parallelization factor for the scrypt function.

Overall, by implementing these changes, we have made the code more resistant to cryptographic attacks and improved the security of the web application.""",
                "Injection":"""Injection refers to a class of vulnerabilities where untrusted user input is passed into an interpreter or compiler as part of a command or query, which can result in unintended actions.

Injection vulnerabilities can be classified into different categories, depending on the type of interpreter or compiler being targeted. Some common types of injection vulnerabilities include:

SQL Injection: In this type of vulnerability, an attacker can inject malicious SQL statements into an application's input field, which can allow them to bypass authentication, access sensitive data, or modify data in the database.

OS Command Injection: In this type of vulnerability, an attacker can inject malicious commands into an application's input field, which can allow them to execute arbitrary commands on the server, leading to a compromise of the system.

LDAP Injection: In this type of vulnerability, an attacker can inject malicious LDAP statements into an application's input field, which can allow them to bypass authentication or access sensitive data.
 
Here's an example of vulnerable code that is susceptible to SQL injection:

 
```python
import mysql.connector

 
# Get user input for username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

 
# Construct an SQL query to retrieve user data
query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)

 
# Execute the query and retrieve the results
cnx = mysql.connector.connect(user='root', password='password', database='mydatabase')
cursor = cnx.cursor()
cursor.execute(query)
results = cursor.fetchall()
```

 
In the code above, the user input for `username` and `password` are used to construct an SQL query without proper input validation and sanitization. An attacker can input SQL commands as the username and password values to execute unintended SQL commands.

 
To fix this vulnerability, we can use parameterized queries, which separate the SQL command and the user input values. Here's an example of fixed code that uses parameterized queries:

 
```python
import mysql.connector

 
# Get user input for username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

 
# Construct a parameterized SQL query to retrieve user data
query = "SELECT * FROM users WHERE username = %s AND password = %s"

 
# Execute the query with user input values
cnx = mysql.connector.connect(user='root', password='password', database='mydatabase')
cursor = cnx.cursor()
cursor.execute(query, (username, password))
results = cursor.fetchall()
```

 
In the code above, we use a parameterized query to separate the SQL command from the user input values. The user input values are passed as a tuple to the `execute` method, which ensures that the user input is properly sanitized and prevents SQL injection attacks.""",
                "Insecure Design":"""Insecure Design refers to vulnerabilities that arise due to design flaws in the web application that lead to security issues.

Insecure Design vulnerabilities can manifest in various ways, including:

Lack of input validation: This vulnerability arises when the web application does not properly validate user input. This can allow attackers to inject malicious code or bypass authentication and gain unauthorized access to the system.

Inadequate access controls: This vulnerability arises when the web application does not properly restrict user access. This can allow attackers to access sensitive information or perform unauthorized actions on the system.

Poor session management: This vulnerability arises when the web application does not properly manage user sessions, such as failing to use secure cookies or not properly expiring sessions. This can allow attackers to hijack user sessions and gain unauthorized access to the system.

Insufficient error handling and logging: This vulnerability arises when the web application does not properly handle errors or log events. This can allow attackers to exploit vulnerabilities and evade detection.

To mitigate Insecure Design vulnerabilities, it is important to adopt secure design principles and practices. Some best practices include:

Input validation: All user input must be validated and sanitized to prevent injection attacks. This includes data such as usernames, passwords, and other user inputs.

Access control: Access controls should be implemented to restrict access to sensitive areas of the system. This includes both user authentication and authorization.

Secure session management: Session management should be implemented to securely manage user sessions. This includes secure cookie handling, session timeouts, and other session management best practices.

Error handling and logging: The web application should properly handle errors and log events to detect and mitigate vulnerabilities.

Secure coding practices: Developers should follow secure coding practices, such as avoiding hard-coded passwords, implementing secure communications, and following secure coding guidelines.

Overall, Insecure Design vulnerabilities can pose a significant risk to the security of web applications. By adopting secure design principles and practices, developers can help mitigate these vulnerabilities and improve the overall security of web applications.
Example code for an insecure design vulnerability:

```

public class Example {
    private int value;
    public Example(int value) {
        this.value = value;
    }
    public int getValue() {
        return value;
    }
}
```

In this example, the `Example` class has a public constructor that takes an integer value and sets it to the `value` field. However, there is no validation on the input value, which means that an attacker can pass a negative value, causing the `getValue()` method to return an unexpected result.

Fixed code:

```
public class Example {
    private int value;
    public Example(int value) {
        if (value < 0) {
            throw new IllegalArgumentException("Value must be positive");
        }
        this.value = value;
    }
    public int getValue() {
        return value;
    }
}

```

In the fixed code, the constructor checks if the input value is negative and throws an exception if it is. This ensures that the `value` field is always initialized with a valid value, preventing unexpected behavior in the `getValue()` method.""",
                "Security Misconfiguration":"""Security Misconfiguration is a vulnerability that arises when a web application or server is configured with default or weak settings. It can happen when security settings are not properly defined or when default passwords are not changed.

Security misconfigurations can lead to unauthorized access to sensitive information, data leaks, and other security breaches. Attackers can exploit these vulnerabilities to access data that should not be public, steal data or modify the website's content.

Some examples of security misconfigurations include:
- Default login credentials left unchanged on servers or applications
- Unnecessary services running on servers
- Outdated software versions with known vulnerabilities
- Improper access controls, such as overly permissive file or directory permissions
- Unsecured APIs (Application Programming Interfaces)

here's an example of OWASP Security Misconfiguration vulnerability and its fixed code:

```python
# Example vulnerable code
import psycopg2

def connect_to_db():
    conn = psycopg2.connect(database="mydatabase", user="myuser", password="mypassword", host="myhost")
    return conn
```

In this example, the code connects to a PostgreSQL database using `psycopg2` library. The database credentials are hardcoded in the function, which is a security misconfiguration vulnerability. If this code is deployed to production, an attacker can easily obtain the credentials by decompiling the code or using a code analysis tool.

Here's the fixed code:

```python
# Fixed code
import os
import psycopg2

def connect_to_db():
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')

    conn = psycopg2.connect(database=db_name, user=db_user, password=db_password, host=db_host)
    return conn
```

In the fixed code, the database credentials are not hardcoded anymore. Instead, they are stored in environment variables, which are retrieved using the `os` module. By storing sensitive information in environment variables, we can ensure that the credentials are not exposed in the source code or logs. Additionally, the use of environment variables makes it easier to manage the credentials, as they can be updated without changing the code.""",
                "Vulnerability and Outdated Components":"""A vulnerability is a weakness or gap in the security measures of a system that could be exploited by attackers to gain unauthorized access, cause a system malfunction, 
or steal sensitive data. Vulnerabilities can exist at various levels of a system, including hardware, software, network, and application layers.
Outdated components refer to software or hardware components that have not been updated to the latest version or patch. These components may contain known vulnerabilities that could be exploited by attackers to compromise the system.
For example, if a web application is using an outdated version of a web server software, it may be vulnerable to attacks that exploit known vulnerabilities in that software. Similarly, if a computer's operating system is not updated with the latest security patches, it may be vulnerable to attacks that exploit known vulnerabilities in that operating system. It is important to keep all components of a system up-to-date to minimize the risk of vulnerabilities being exploited by attackers.

Here's an example code snippet that contains a vulnerability due to an outdated component:

```python
import requests

def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=123456".format(city)
    response = requests.get(url)
    return response.json()

print(get_weather("London"))
```

In this code, we are using the `requests` library to make an API call to get weather data for a specific city. However, the code is using an outdated version of the library (`requests` version 2.0.0) that contains a known vulnerability. 
To fix this vulnerability, we need to update the `requests` library to a newer version that does not contain the vulnerability. Here's the fixed code:

```python
import requests

def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=123456".format(city)
    response = requests.get(url)
    return response.json()

print(get_weather("London"))
```

In this fixed code, we have updated the `requests` library to the latest version (currently 2.26.0) which does not contain the known vulnerability. By keeping our dependencies up-to-date, we can avoid known vulnerabilities and ensure the security of our code.""",
                "Identification and Authentication Failures":"""Identification and authentication failures are a significant vulnerability that can lead to unauthorized access to sensitive systems and data. When users fail to provide the necessary credentials or when fraudulent users impersonate legitimate users, attackers can exploit these failures to gain access to the system.

These vulnerabilities can occur in various forms, including:
Weak passwords: Weak passwords are the most common cause of identification and authentication failures. Attackers can use brute-force attacks or password cracking tools to guess weak passwords or steal them through phishing attacks.

Lack of multifactor authentication: Multifactor authentication provides an additional layer of security to verify the identity of the user. Without multifactor authentication, an attacker can gain access to the system with just a username and password.

Ineffective password policies: Password policies that allow users to choose weak passwords or do not require password changes frequently are vulnerable to attacks.

Insufficient account lockout mechanisms: Account lockout mechanisms that do not lock out user accounts after a specified number of failed login attempts can be exploited by attackers to perform brute-force attacks.

Lack of user account management: Poor user account management practices such as failing to disable inactive accounts or deleting accounts of former employees can lead to unauthorized access.

Social engineering attacks: Social engineering attacks such as phishing can trick users into revealing their login credentials, bypassing identification and authentication mechanisms.

To prevent identification and authentication failures, organizations should follow best practices such as:

Implement strong password policies: Password policies should require users to choose strong passwords that include a mix of uppercase and lowercase letters, numbers, and special characters. Passwords should also be changed regularly.

Implement multifactor authentication: Multifactor authentication should be used to add an extra layer of security to the identification and authentication process.

Implement account lockout mechanisms: Account lockout mechanisms should be implemented to lock out user accounts after a specified number of failed login attempts.

Implement user account management practices: User account management practices should be implemented to ensure that inactive accounts are disabled and former employees' accounts are deleted.

Educate users: Users should be educated about social engineering attacks and trained on best practices for identifying and avoiding them.

The consequences of identification and authentication failures can be severe, ranging from unauthorized access to sensitive data and systems to data breaches and loss of critical business information. Attackers can use the compromised credentials to launch further attacks or steal sensitive information, compromising the confidentiality, integrity, and availability of the system and its data.

To mitigate the risk of identification and authentication failures, organizations must implement robust authentication mechanisms, including strong passwords, multi-factor authentication, and regular employee training and awareness programs. Regular monitoring and auditing of authentication logs can help detect suspicious activity and prevent unauthorized access before it causes significant damage. Additionally, it is essential to have incident response plans in place to address any security incidents promptly and minimize their impact.


An example of identification and authentication failure can be seen in the following code snippet:

 
```
username = request.POST['username']
password = request.POST['password']

 
if username == 'admin' and password == 'password':
    # grant admin access
else:
    # deny access
```
In the above code, the username and password are submitted via a POST request. However, the code does not perform any validation on the username or password to ensure that the user is who they claim to be. An attacker could simply submit any username and password values to gain access.
To fix this vulnerability, the application should implement proper identification and authentication mechanisms, such as password hashing and salting, two-factor authentication, or the use of security tokens. Additionally, the code should validate the credentials provided by the user against a secure authentication source, such as a database of authorized users.
 

A fixed version of the above code could look like this:
 

```
username = request.POST['username']
password = request.POST['password']
 

# Hash and salt the password before validating it
hashed_password = hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()


# Validate the username and password against a secure authentication source
if authenticate_user(username, hashed_password):
    # grant access
else:
    # deny access
```

 
In the above code, the password is hashed and salted before being validated against a secure authentication source. This ensures that even if an attacker obtains the hashed password, they will not be able to use it to gain access. The `authenticate_user` function should be implemented to validate the provided credentials against a secure source, such as a database of authorized users.""",
                "Software and Data Integrity Failures":"""Software and data integrity failures are a vulnerability that can occur when software and data are modified or altered without authorization or in an unintended manner. These failures can lead to data corruption, loss of data, and unauthorized access to systems and data.

Software integrity failures can occur due to various reasons, including software bugs, design flaws, programming errors, and malware. These failures can lead to unauthorized modification of software code, which can result in the execution of unintended functions, alteration of program logic, or unauthorized data access. Attackers can exploit these vulnerabilities by injecting malicious code or by modifying existing code to achieve their objectives.

Data integrity failures can occur due to various reasons, including accidental or intentional modifications, human error, system failures, and cyber-attacks. These failures can lead to data corruption, data loss, or unauthorized data access. Attackers can exploit these vulnerabilities by tampering with data or by introducing malicious data into the system.

The consequences of software and data integrity failures can be severe, including system downtime, loss of critical data, and unauthorized access to sensitive systems and data. These failures can also compromise the confidentiality, integrity, and availability of the system and its data, leading to reputational damage, financial loss, and legal liabilities.

To mitigate the risk of software and data integrity failures, organizations should implement measures such as:

Code review: Organizations should conduct regular code reviews to identify and fix software vulnerabilities. Code reviews can help detect programming errors, design flaws, and other software vulnerabilities before they are introduced into the system.

Software testing: Organizations should conduct regular software testing to ensure that software functions as intended and is free from vulnerabilities. Testing can help detect software bugs, design flaws, and other software vulnerabilities that can compromise software and data integrity.

Access controls: Organizations should implement access controls to prevent unauthorized access to software and data. Access controls can help restrict access to sensitive systems and data to authorized personnel only.

Data backup and recovery: Organizations should implement a data backup and recovery plan to prevent data loss due to software and data integrity failures. Regular backups can help ensure that data can be restored in case of data loss or corruption.

Security monitoring and incident response: Organizations should implement security monitoring and incident response plans to detect and respond to security incidents promptly. Monitoring can help detect unauthorized access and data tampering, while incident response plans can help organizations respond to security incidents and minimize their impact.

 
Example Code:
```python
import hashlib

 
def verify_password(user_input_password):
    password = "MySecretPassword"
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    if hashed_password == user_input_password:
        print("Login successful")
    else:
        print("Login failed")

 
user_input = input("Enter password: ")
verify_password(user_input)
```
In the above example code, the password is being hashed using a weak hashing algorithm (SHA-256) without using any salt, making it vulnerable to a hash collision attack. An attacker can easily retrieve the original password by using a dictionary or brute-force attack, compromising the integrity of the password and the system.

 
Fix Code:
```python
import hashlib
import secrets


def verify_password(user_input_password):
    password = "MySecretPassword"
    salt = secrets.token_hex(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    if hashed_password.hex() == user_input_password:
        print("Login successful")
    else:
        print("Login failed")
 

user_input = input("Enter password: ")
verify_password(user_input)
```
In the fixed code, a strong key derivation function (PBKDF2-HMAC-SHA256) is used with a random salt generated using the `secrets` module. The number of iterations is set to 100,000 to increase the computational cost of a brute-force attack. This makes it more difficult for an attacker to retrieve the original password, thus improving the integrity of the password and the system.""",
                "Security Logging and Monitoring Failures":"""Security logging and monitoring failures refer to the inability of an organization to detect security incidents due to insufficient or ineffective logging and monitoring of its IT systems. These failures can result in the organization being unable to detect security incidents in a timely manner or at all, and can lead to unauthorized access, data breaches, and other security incidents.

Some common causes of security logging and monitoring failures include:

Insufficient logging: If an organization is not logging enough information about its IT systems, it may miss important security events or incidents that can compromise its security. For example, if a system is not configured to log all failed login attempts, an attacker could attempt to guess passwords without being detected.

Ineffective monitoring: Even if an organization is logging enough information about its IT systems, it may not be effectively monitoring those logs for signs of security incidents. This can occur if the organization lacks the necessary resources or expertise to monitor its logs or if it has implemented ineffective monitoring processes.

Lack of context: Logging and monitoring data in isolation may not provide the context necessary to detect security incidents. For example, a failed login attempt may not be a cause for concern on its own, but if it is followed by multiple failed attempts from the same IP address, it may indicate a brute-force attack.

Poor log management: If an organization is not managing its logs properly, it may not be able to effectively analyze them for signs of security incidents. Poor log management can include issues such as log files being overwritten too quickly, logs being stored in an unsecured location, or logs not being backed up regularly.

The consequences of security logging and monitoring failures can be severe. Without proper logging and monitoring, organizations may not be able to detect security incidents in a timely manner or at all. This can result in sensitive data being compromised, systems being taken offline, and damage to an organization's reputation and bottom line.

To mitigate the risk of security logging and monitoring failures, organizations should implement measures such as:

Logging best practices: Organizations should follow best practices for logging, such as logging all security-related events, including successful and unsuccessful login attempts, changes to system configurations, and other critical events.

Effective monitoring: Organizations should implement effective monitoring processes, such as real-time monitoring and automated alerting, to detect security incidents as they occur.

Contextual analysis: Organizations should analyze logs in context to detect security incidents. This can involve correlating events across multiple systems or analyzing log data in conjunction with other security data sources.

Log management: Organizations should manage logs effectively, including storing logs in a secure location, backing up logs regularly, and setting retention policies that are appropriate for the organization's needs.

Incident response: Organizations should have a robust incident response plan in place that outlines the steps to be taken in the event of a security incident. This plan should include processes for logging and monitoring during and after an incident to ensure that all relevant information is captured.
 

Example code:

 
```python
import logging


# Some code here
user = "admin"
logging.info("User %s logged in", user)
# Some more code here
```

 
In the above code, we are logging the user's login information using the `logging` module in Python. However, if the logs are not properly maintained, or if the logs are not monitored regularly, it can result in the failure to detect and respond to security incidents in a timely manner.


Fixed code:


```python
import logging


# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

 
# Create a file handler
handler = logging.FileHandler("app.log")
handler.setLevel(logging.INFO)


# Create a log format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

 
# Add the file handler to the logger
logger.addHandler(handler)


# Some code here
user = "admin"
logger.info("User %s logged in", user)
# Some more code here
```

 
In the fixed code, we have created a logger object, set the logging level to `INFO`, created a file handler to log the messages to a file, set the log format, and added the file handler to the logger object. This ensures that the logs are maintained properly, and can be monitored regularly to detect and respond to security incidents in a timely manner.""",
                "Servere-Side Request Forgery":"""Server-side request forgery (SSRF) is a type of vulnerability that allows an attacker to send unauthorized requests from a vulnerable server to other internal or external servers. The vulnerability occurs when a web application takes user input and uses it to make requests to other servers, without properly validating or sanitizing the input.

An attacker can exploit SSRF to:

Access unauthorized resources: An attacker can use SSRF to access internal resources that should not be accessible from outside the network, such as databases or other servers.

Bypass access controls: An attacker can use SSRF to bypass access controls that are in place to prevent access to sensitive resources.

Perform denial of service attacks: An attacker can use SSRF to overload servers or applications by sending large volumes of requests to them.

Execute arbitrary code: An attacker can use SSRF to execute arbitrary code on a vulnerable server by exploiting vulnerabilities in the server's software.

There are several ways in which SSRF can be exploited. One common method is to use a vulnerable web application to send a request to a local or internal IP address that should not be accessible from outside the network. This can allow an attacker to access sensitive resources, such as databases or other servers, that are located within the organization's internal network.

Another method is to use SSRF to bypass access controls. For example, an attacker can use SSRF to send requests to a web server that is only accessible from within the organization's network, and then use that server to access resources that are only accessible from that server.

To prevent SSRF vulnerabilities, developers should follow best practices such as:

Validate and sanitize user input: Developers should validate and sanitize all user input to ensure that it does not contain any malicious code or unauthorized requests.

Use whitelists: Developers should use whitelists to limit the destinations to which requests can be sent. For example, a web application may only be allowed to send requests to a specific set of servers, and all other requests should be blocked.

Use secure coding practices: Developers should use secure coding practices to minimize the risk of vulnerabilities, such as input validation and output encoding.

Limit network access: Developers should limit the network access of their servers and applications to reduce the attack surface of their systems.

 
An example of code vulnerable to SSRF could look like this:
 

```python
import requests
 

def get_data(url):
    r = requests.get(url)
    return r.text
```
 

In this code, the `get_data` function takes a URL as an argument, and then uses the `requests` library to make a GET request to that URL and return the response text. However, if an attacker is able to manipulate the URL parameter, they could potentially send a request to an internal network resource.
 

A fix for this vulnerability could involve adding input validation to ensure that the URL being requested is an allowed domain, or using a whitelist of allowed URLs. Additionally, it may be necessary to restrict access to sensitive internal network resources from external requests. Here's an example of a fixed code:

 
```python
import requests
 

def get_data(url):
    allowed_domains = ['example.com', 'api.example.com']
    if not any(domain in url for domain in allowed_domains):
        raise ValueError('Invalid URL')
    r = requests.get(url)
    return r.text
```

 
In this code, we define a list of allowed domains, and then check to see if the requested URL contains one of those domains. If the URL is not allowed, we raise a `ValueError`. This prevents an attacker from being able to make unauthorized requests to internal resources."""
               }


# Create a dictionary for OWASP Top 10 API Vulnerabilities
owasp_top_10_api_vulns = {"Broken Object Level Authorization":""" APIs that expose endpoints that handle object identifiers may create a wide attack surface for attackers to exploit. Object level authorization checks should be considered in every function that accesses a data source using an input from the user. Without proper object-level authorization checks, attackers can bypass the intended access controls and access or modify data they should not be allowed to.

Example: An attacker sends a request to an API endpoint that retrieves user profile information by supplying a user ID in the request URL. However, the API does not perform proper authorization checks to ensure that the authenticated user has permission to access the requested user's profile. As a result, the attacker can access and retrieve the private profile information of other users.""",
                  "Broken User Authentication":""" Authentication mechanisms are often implemented incorrectly, allowing attackers to compromise authentication tokens or to exploit implementation flaws to assume other user's identities temporarily or permanently. Compromising a system's ability to identify the client/user compromises API security overall. Proper implementation of user authentication measures, such as strong password policies, multi-factor authentication, and secure token handling, can help prevent these attacks.
                  
Example: An API implements an authentication mechanism that uses session tokens to identify and authenticate users. However, the API fails to properly validate and secure these tokens, allowing an attacker to steal a valid token and use it to impersonate the authenticated user and perform unauthorized actions.""",
                  "Excessive Data Exposure":""" Developers often expose all object properties without considering their individual sensitivity, relying on clients to perform the data filtering before displaying it to the user. Attackers can exploit this vulnerability by accessing sensitive data through unauthorized endpoints, bypassing proper authentication and authorization controls. Developers should consider the sensitivity of each object property and restrict access accordingly.
                  
Example: An API exposes sensitive data, such as a user's social security number, in its responses without proper data filtering or masking. This could allow an attacker to easily access and obtain this sensitive data.""",
                  "Lack of Resources & Rate Limiting":"""APIs often do not impose any restrictions on the size or number of resources that can be requested by the client/user. This can lead to performance issues, such as Denial of Service (DoS), and also leave the door open to authentication flaws such as brute force attacks. Properly implemented resource and rate limiting can help prevent these attacks.
                  
Example: An API does not enforce any limits on the number of requests a user can make, allowing an attacker to launch a brute force attack against an authentication endpoint to guess valid login credentials.""",
                  "Broken Function Level Authorization":"""Complex access control policies with different hierarchies, groups, and roles, and an unclear separation between administrative and regular functions, tend to lead to authorization flaws. By exploiting these issues, attackers gain access to other users' resources and/or administrative functions. Developers should consider separating administrative functions from regular functions and implementing appropriate access controls.
                  
Example: An API endpoint is supposed to be accessible only to administrators, but due to a flaw in the access control logic, regular users are able to access and modify sensitive data through this endpoint.""",
                  "Mass Assignment":"""Binding client provided data (e.g., JSON) to data models without proper properties filtering based on an allowlist usually leads to Mass Assignment. Attackers can modify object properties they are not supposed to by guessing objects properties, exploring other API endpoints, reading the documentation, or providing additional object properties in request payloads. Developers should validate user input and filter out any unnecessary data before processing it.
                  
Example: An API endpoint accepts user input as JSON and directly maps the input to an object without validating or sanitizing the input. An attacker can then supply additional properties in the JSON payload that the API will accept and use to modify the object's properties, allowing the attacker to modify sensitive data or perform unauthorized actions.""",
                  "Security Misconfiguration":"""Security misconfiguration is commonly a result of unsecure default configurations, incomplete or ad-hoc configurations, open cloud storage, misconfigured HTTP headers, unnecessary HTTP methods, permissive Cross-Origin resource sharing (CORS), and verbose error messages containing sensitive information. Properly configured security settings can help prevent these types of attacks.
                  
Example: An API has an unsecured default configuration that allows an attacker to bypass authentication checks and gain access to sensitive data or functionality.""",
                  "Injection":"""Injection flaws occur when untrusted data is sent to an interpreter as part of a command or query. Attackers can exploit these vulnerabilities by tricking the interpreter into executing unintended commands or accessing data without proper authorization. Developers should use parameterized queries and input validation to prevent injection attacks.
                  
Example: An API endpoint uses unvalidated user input to construct a SQL query that is sent to a database server. An attacker can supply malicious input that causes the database server to execute unintended SQL commands, such as deleting or modifying data.""",
                  "Improper Assets Management":"""APIs tend to expose more endpoints than traditional web applications, making proper and updated documentation highly important. Proper hosts and deployed API versions inventory also play an important role in mitigating issues such as deprecated API versions and exposed debug endpoints. Properly managed assets can help prevent these types of attacks.
                  
Example: An API has outdated or deprecated endpoints that are no longer in use, but are still accessible and contain sensitive data or functionality that can be exploited by an attacker.""",
                  "Insufficient Logging & Monitoring":"""This vulnerability occurs when APIs do not log enough information about user activity or do not monitor user activity for suspicious behavior. Without proper logging and monitoring, it is difficult to detect and respond to security breaches in a timely manner, which can result in sensitive data being compromised.
                  
Example: An API does not log important security events or activities, such as failed login attempts or unauthorized access attempts. This makes it difficult to detect and respond to security incidents in a timely manner, allowing an attacker to maintain persistence and further compromise the system."""
                 }


# Initialise session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": content_message}
    ]
if 'cost' not in st.session_state:
    st.session_state['cost'] = []
if 'total_tokens' not in st.session_state:
    st.session_state['total_tokens'] = []  # Initialize the 'total_tokens' list
if 'total_cost' not in st.session_state:
    st.session_state['total_cost'] = 0.0
if "button_clicked" not in st.session_state:
    st.session_state["button_clicked"] = False    

    
# Sidebar

validate_button = st.sidebar.button("Validate Code", key="validate")

if validate_button:
    st.session_state["button_clicked"] = True

# Create a selectbox for vulnerability types
vuln_type = st.sidebar.selectbox(
    "Select a vulnerability type",
    ("Select a vulnerability type","OWASP Top 10 Vulnerabilities", "OWASP Top 10 API Vulnerabilities"),
    index = 0
)


# Display the selected vulnerability type
if vuln_type == "OWASP Top 10 Vulnerabilities":
    st.sidebar.write("## OWASP Top 10 Vulnerabilities")
    vuln = st.sidebar.selectbox(
        "Select a vulnerability",
        ["Select a vulnerability"]+list(owasp_top_10_vulns.keys()),
        index = 0,
        key="vuln_selector"
    )
    if vuln != "Select a vulnerability":
        st.write(f"### {vuln}")
        st.write(owasp_top_10_vulns[vuln])

elif vuln_type == "OWASP Top 10 API Vulnerabilities":
    st.sidebar.write("## OWASP Top 10 API Vulnerabilities")
    vuln = st.sidebar.selectbox(
        "Select a vulnerability",
        ["Select a vulnerability"]+list(owasp_top_10_api_vulns.keys()),
        index = 0,
        key="vuln_selector"
    )
    if vuln != "Select a vulnerability":
        st.write(f"### {vuln}")
        st.write(owasp_top_10_api_vulns[vuln])
        
# shows total cost of the conversation and a button to clear the conversation                         
counter_placeholder = st.sidebar.empty()
counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
clear_button = st.sidebar.button("Clear Conversation", key="clear")
            
# reset everything
if clear_button:
    st.session_state['generated'] = []
    st.session_state['past'] = []
    st.session_state['messages'] = [
        {"role": "system", "content": content_message}
    ]
    st.session_state['number_tokens'] = []
    st.session_state['cost'] = []
    st.session_state['total_cost'] = 0.0
    st.session_state['total_tokens'] = []
    st.session_state["button_clicked"] = False
    counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")

    
# generate a response
def generate_response(prompt):
    st.session_state['messages'].append({"role": "user", "content": prompt})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state['messages']
    )
    response = completion.choices[0].message.content.strip()
    if not response.lower().startswith("i'm sorry"):
        st.session_state['messages'].append({"role": "assistant", "content": response})
    else:
        st.session_state['messages'][-1]["content"] = content_message

    total_tokens = completion.usage.total_tokens
    prompt_tokens = completion.usage.prompt_tokens
    completion_tokens = completion.usage.completion_tokens
    return response, total_tokens, prompt_tokens, completion_tokens    

# container for chat history
response_container = st.container()


if st.session_state["button_clicked"]:
    # container for text box
    container = st.container()
    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_area("You:", key='input', height=100)
            submit_button = st.form_submit_button(label='Send')

            if submit_button and user_input:
                output, total_tokens, prompt_tokens, completion_tokens = generate_response(user_input)
                st.session_state['past'].append(user_input)
                st.session_state['generated'].append(output)
                st.session_state['total_tokens'].append(total_tokens)

                # from https://openai.com/pricing#language-models
                cost = total_tokens * 0.002 / 1000

                st.session_state['cost'].append(cost)
                st.session_state['total_cost'] += cost

    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
                message(st.session_state["generated"][i], key=str(i))
                st.write(
                    f"Number of tokens: {st.session_state['total_tokens'][i]}; Cost: ${st.session_state['cost'][i]:.5f}")
                counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
                
