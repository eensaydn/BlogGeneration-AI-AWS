# 🚀 AI Blog Generator

A serverless blog content generation system powered by AWS services and Amazon Bedrock's generative AI capabilities. This end-to-end solution automatically creates high-quality blog posts from simple topic inputs and stores them in cloud storage.

## 🎯 Overview

The AI Blog Generator is a production-ready serverless application that leverages Meta's Llama3-70B model through Amazon Bedrock to generate contextually relevant blog content. The system provides a RESTful API interface that accepts blog topics and returns professionally written content, automatically saved to Amazon S3 for persistence.

## 🏗️ Architecture

```
Client (Postman) → API Gateway → Lambda Function → Amazon Bedrock → S3 Storage
                                      ↓
                               CloudWatch Logs
```

### Core Components

- **API Gateway**: RESTful endpoint management and request routing
- **AWS Lambda**: Serverless compute with custom runtime layers
- **Amazon Bedrock**: AI content generation using Meta Llama3-70B
- **Amazon S3**: Persistent storage with organized file structure
- **CloudWatch**: Comprehensive logging and monitoring

## ✨ Features

- **Intelligent Content Generation**: Leverages Meta Llama3-70B for high-quality blog posts
- **Serverless Architecture**: Fully managed, scalable, and cost-effective
- **Automated Storage**: Generated content automatically saved with timestamps
- **RESTful API**: Clean, documented endpoints for easy integration
- **Comprehensive Logging**: Full request/response tracking via CloudWatch
- **Custom Runtime**: Optimized Lambda layers for enhanced performance

## 🛠️ Technology Stack

- **Backend**: Python 3.9, boto3
- **Cloud Provider**: Amazon Web Services (AWS)
- **AI/ML**: Amazon Bedrock, Meta Llama3-70B
- **Storage**: Amazon S3
- **API**: AWS API Gateway
- **Compute**: AWS Lambda
- **Monitoring**: CloudWatch Logs
- **Testing**: Postman

## 📋 Prerequisites

- AWS Account with appropriate permissions
- AWS CLI configured
- Python 3.9+
- boto3 library
- Access to Amazon Bedrock service
- S3 bucket for content storage

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/eensaydn/ai-blog-generator.git
cd ai-blog-generator
```

### 2. Set Up AWS Resources

Create an S3 bucket:
```bash
aws s3 mb s3://your-blog-bucket-name
```

### 3. Deploy Lambda Function

1. Package the Lambda function with dependencies
2. Create custom Lambda layer if needed
3. Deploy using AWS CLI or Console
4. Configure environment variables

### 4. Configure API Gateway

1. Create new REST API
2. Configure POST method
3. Set up Lambda integration
4. Deploy to stage

### 5. Test the API

```json
POST /blog-generation
{
    "blog_topic": "The Future of Artificial Intelligence"
}
```

## 📖 API Documentation

### Generate Blog Post

**Endpoint**: `POST /blog-generation`

**Request Body**:
```json
{
    "blog_topic": "Your blog topic here"
}
```

**Response**:
```json
{
    "statusCode": 200,
    "body": "Blog Generation is completed"
}
```

**Generated Content**: Automatically saved to S3 as timestamped `.txt` files in the `blog-output/` folder.

## 🔧 Configuration

### Environment Variables

- `S3_BUCKET_NAME`: Target S3 bucket for content storage
- `AWS_REGION`: AWS region for Bedrock service (default: us-east-2)
- `MODEL_ID`: Bedrock model identifier (default: meta.llama3-70b-instruct-v1:0)

### Lambda Function Settings

- **Runtime**: Python 3.9
- **Memory**: 512 MB (recommended)
- **Timeout**: 30 seconds
- **Custom Layer**: Required for additional dependencies

## 📊 Monitoring

The application includes comprehensive logging through CloudWatch:

- API Gateway request/response logs
- Lambda function execution logs
- Error tracking and debugging information
- Performance metrics and insights

## 🔒 Security Considerations

- IAM roles with least privilege principles
- API Gateway with proper authentication (implement as needed)
- S3 bucket policies for controlled access
- CloudWatch logs retention policies

## 🎯 Use Cases

- **Content Marketing**: Automated blog post generation for marketing teams
- **Educational Content**: Quick article creation for learning platforms
- **Prototype Development**: Rapid content generation for MVPs
- **Research**: AI-powered content analysis and generation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Enes Aydın**
- GitHub: [@eensaydn](https://github.com/eensaydn)
- LinkedIn: [enesaydin00](https://www.linkedin.com/in/enesaydin00)

## 🙏 Acknowledgments

- Amazon Web Services for the robust cloud infrastructure
- Meta for the powerful Llama3-70B language model
- The open-source community for continuous inspiration

---

⭐ **Star this repository if you found it helpful!**
