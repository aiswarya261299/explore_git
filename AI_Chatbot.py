#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import openai
import re

# Set up OpenAI API key
openai.api_key = "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"

# Prompt engineering
query=""
prompt = """Given a program, provide the details  of the vulnerability and the corresponding fixes. for example an OWASP code vulnerability buffer overflow in a C++ code looks like this:
void copy_string(char* dest, const char* src) {
    while (*src != '\0') {
        *dest = *src;
        ++dest;
        ++src;
    }
    *dest = '\0';
}

int main() {
    char buffer[10];
    const char* str = "Hello, world!";
    copy_string(buffer, str);
    return 0;
}

In this code, the copy_string function takes two arguments: a destination buffer dest and a source string src. The function copies the contents of src into dest until it encounters a null terminator ('\0'). However, the main function declares a buffer of only 10 characters, while the src string is much longer than that. This means that if the copy_string function is called with buffer as the dest argument and str as the src argument, the function will write more than 10 characters into the buffer, causing a buffer overflow vulnerability.

To fix this vulnerability, the copy_string function should include a check to ensure that the destination buffer has enough space to hold the entire source string.

similiarly analyse the following code and give:

%s

1. Name the vulnerability in the code and explain the vulnerability.
2. Give the solution for this vulnerability"""

# Create a multi-line text input for code
input_type = st.radio("Select input type", options=["Text", "File"])

if input_type == "Text":
    code = st.text_area("Enter your code here:", height=200)
    query = ""
    # Check if the text contains common code patterns
    if code:
        query = prompt%(code)
        lines = code.split("\n")
        # Split the text into lines
        valid = False
        for line in lines:
            # Process each line of text
            if re.search(r"\b(def|class|import|print)\b", line) or                 re.search(r"[()\[\];{},]", line):
                valid = True
            else:
                valid = False
                break
        if valid:
            st.success("Your input appears to be valid code!")
        else:
            st.error("Your input does not appear to be valid code.")
elif input_type == "File":
    # Create a file uploader that only accepts code files
    uploaded_file = st.file_uploader("Upload a file",
                                     type=['.py', '.js', '.cpp', '.h', '.cs', '.java', '.rb', '.php', '.go', '.swift',
                                           '.ts', '.sql', '.sh', '.html', '.htm', '.css', '.xml', '.json']
                                    )
    # Check if a file was uploaded
    if uploaded_file is not None:
        # Read the contents of the file
        file_contents = uploaded_file.read().decode("utf-8")
        # Display the contents of the file
        st.write("File contents:")
        st.code(file_contents)
        query = prompt%(file_contents)
        
if query:
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=query,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    result = response.choices[0].text
    # Display the result
    st.write("Response:")
    st.write(result)
    
    # Continue the conversation based on the response
    counter = 0
    while True:
        counter += 1
        continuation = st.text_input("Enter your response:", key=counter)
        if continuation:
            query = result.strip() + "\n" + continuation.strip()
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=query,
                max_tokens=1000,
                n=1,
                stop=None,
                temperature=0.5,
            )
            result = response.choices[0].text
            # Display the result
            st.write("Response:")
            st.write(result)
        else:
            break


# In[ ]:




