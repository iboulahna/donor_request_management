# donor_request_management


# **Automated Donor Request Management System**

This project aims to automate the response to donor requests for charitable organizations. By implementing a Generative AI (GenAI) model and a Retrieval-Augmented Generation (RAG) system, the solution will handle 90% of common donor queries while reducing reliance on third-party call centers, saving an estimated €50,000 annually.

## **Project Objective**
The system aims to automate responses to common donor requests such as:
- Increasing monthly donations
- Stopping or suspending donations
- Requesting fiscal receipts

For more complex queries, the system will transfer the request to a human advisor within the organization.

## **Architecture Overview**

### **1. Speech-to-Text Conversion**
- **Functionality**: Donor requests are captured as phone calls, which are transcribed to text using a speech-to-text service.
- **Tools**:
  - **Google Cloud Speech-to-Text** or **AWS Transcribe**

### **2. GenAI Model for Query Understanding and Response Generation**
- **Functionality**: Uses a Generative AI model (such as GPT-4) to understand the donor's request and generate a response for 90% of common queries.
- **Tools**:
  - **OpenAI GPT-4 API**
  - **Flask** or **Django** for API management

### **3. Retrieval-Augmented Generation (RAG)**
- **Functionality**: Augments responses by fetching relevant data (e.g., donor status, donation history) before generating an answer.
- **Tools**:
  - **Vector Search** (e.g., **FAISS**, **Pinecone**, or **Elasticsearch**) for searching relevant information
  - **LangChain** or **Haystack** for integrating search and generation

### **4. Transfer Complex Requests to Human Advisors**
- **Functionality**: For complex or sensitive requests, the system flags the query and redirects it to a human advisor.
- **Tools**:
  - **Flask** or **Django** for API handling
  - **Database** (e.g., **PostgreSQL** or **MongoDB**) for tracking query status

### **5. Query Tracking and Analytics**
- **Functionality**: Logs all requests and responses for monitoring, performance analysis, and future improvements.
- **Tools**:
  - **Database** (e.g., **PostgreSQL**, **MongoDB**)
  - **Monitoring tools** like **Grafana** or **Kibana**

## **How It Works**

1. **Capture Requests**: Donors call the organization’s customer service line. The voice input is converted to text using the speech-to-text service.
2. **Query Understanding**: The transcribed query is sent to the GenAI model, which generates an appropriate response.
3. **RAG Integration**: The system searches the relevant database (e.g., donor records, common FAQs) to augment the response with personalized information.
4. **Response Delivery**: If the system generates a sufficient response, it is sent back to the donor. If the query is too complex, it is flagged for transfer to a human advisor.
5. **Tracking**: All interactions are logged for reporting and to improve the system over time.

## **Tech Stack**

- **Speech-to-Text**: AWS Transcribe
- **Generative AI**: OpenAI GPT-4 API
- **API Management**: Flask
- **Search & Retrieval**: Pinecone 
- **Data Processing & Analytics**: LangChain (for RAG)
- **Monitoring**: Prometheus (for logs), Grafana

## **Setup Instructions**

### **1. Install Dependencies**

Install required Python packages:

```bash
pip install openai google-cloud-speech flask langchain faiss-cpu pinecone-client
```

For Speech-to-Text, you'll need to set up your Google Cloud credentials:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path_to_your_google_credentials.json"
```

### **2. Google Cloud Speech-to-Text Setup**

Follow the [Google Cloud Speech-to-Text setup guide](https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries) to create a project and enable the Speech-to-Text API.

### **3. OpenAI GPT-4 API Setup**

Sign up for an API key from [OpenAI](https://beta.openai.com/signup/) and set the key in your environment:

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

### **4. Running the Application**

To run the Flask application, use:

```bash
python app.py
```

This will start the API that handles incoming requests.

### **5. Sample Request**

You can test the system by sending a POST request with a donor query:

```bash
curl -X POST http://127.0.0.1:5000/handle_request     -H "Content-Type: application/json"     -d '{"query": "I would like to increase my monthly donation."}'
```


## **Contributing**

Feel free to fork this repository and submit pull requests. If you have any suggestions, issues, or improvements, please open an issue on the GitHub repository.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
