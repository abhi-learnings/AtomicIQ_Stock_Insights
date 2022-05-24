# AtomicIQ_Stock_Insights

**Requirement:**

Develop an application in python to retrieve summary of stock insights for various stocks listed at NSE, BSE & Nifty50 on their email.

End User should be able to :
•	Retrieve results with the help of a single click
•	View current market price of the stocks
•	View 52 week high of the stocks
•	View 52 week low of the stocks
•	Receive a summary of the result through email.

The application needs to be containerized using Docker and then deployed on AWS EC2. 
Once the docker image is ready, create a pod using the same image with 2 replicas (Use Kubeadm to create a single node cluster)

======================================================================================
**Approach:**
1. Create python script file - AtomicIQ_Stock_Insights.py
2. Create docker image using docker file
3. Test docker images by running container.
4. EKS cluster deploy the application .
5. Application URL :http://35.154.14.16:31427/
