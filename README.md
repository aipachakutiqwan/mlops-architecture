# MLOps-architecture

This repository describe the Bestseller MLOps implementation for planning application case which manage delivery and replenishment of products to their customers.

#### 1. Describe the minimal requirements of an MLOps platform and their importance

The details of the minimal requirements for a good MLOps in production are described below.

- Continuous Integration and Continuous Deployment (CI/CD): Integration with CI/CD pipelines to automate the process of building, testing, and deploying machine learning models, enabling rapid iteration and delivery.

- Automated Testing and Validation: Frameworks for automating testing and validation of machine learning models throughout the development lifecycle, including unit tests, integration tests, and validation against historical data.

- Model Versioning and Tracking: A system for tracking different versions of machine learning models, including the ability to store metadata such as training data, hyperparameters, and evaluation metrics associated with each version.

- Model Deployment: Tools for packaging trained machine learning models into deployable artifacts and deploying them to production environments.

- Model Serving and Inference: Infrastructure for serving predictions from deployed machine learning models at scale, including support for real-time and batch inference, load balancing, and fault tolerance.

- Scalability and Performance Monitoring: Capabilities for monitoring the performance of deployed models in real-time, including metrics like latency, throughput, and accuracy, to ensure they meet service-level objectives (SLAs).

- Model Monitoring and Drifting Detection: Mechanisms for monitoring model performance in production environments and detecting anomalies or drift in input data or model behavior, which may indicate the need for model retraining or intervention.

- Human-in-the-loop and Model Improvement: Mechanisms for collecting human feedback and incorporating it into the model improvement cycle, facilitating continuous learning and adaptation to changing conditions.

- Security and Compliance: Features for ensuring the security and compliance of machine learning systems, including access control, data encryption, audit logging, and compliance with regulatory requirements.


#### 2. MLOps Architecture for an ML-driven planning tool

The nex figure describe the principal MLOps components and  its  integration with the BestSeller planning  tool. This architecture consider the MLOps requirements described above and two integrations patterns: Orchestrator (Directed Acyclic Graph) for the ML workloads integration and Choreography for the data input and ouput.

![BestSeller Mlops](./docs/bestseller-mlops.png?  "BestSeller Mlops Architecture")

#### 3. Online Endpoint Microservice

A Fast API online endpoint for Food Delivery Duration Predictor was created and exposed on the port 8080. The input to the model are composed for the following list of features:

```console

    id: str
    delivery_person_age: float
    delivery_person_ratings: float
    restaurant_latitude: float
    restaurant_longitude: float
    delivery_location_latitude: float
    delivery_location_longitude: float
    weather_conditions: int
    road_traffic_density: int
    vehicle_condition: int
    type_of_order: int
    type_of_vehicle: int
    multiple_deliveries: float
    festival: int
    city: int
    city_code: int
    day: int
    month: int
    quarter: int
    year: int
    day_of_week: int
    is_month_start: int
    is_month_end: int
    is_quarter_start: int
    is_quarter_end: int
    is_year_start: int
    is_year_end: int
    is_weekend: int
    order_prepare_time: float
    distance: int

 ```


For activate the inference enpoint it is required to follow the next steps.

- Build and run the docker image in the terminal.
```console
 docker compose up 
 ```

- Verify the service is running on the port 8080.

```console
mlops-architecture-predictor-1  | INFO:     Application startup complete.
mlops-architecture-predictor-1  | [Tech] 2024-03-15 03:37:07,937 - INFO - Application startup complete.
mlops-architecture-predictor-1  | [Tech] 2024-03-15 03:37:07,938 - INFO - Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
mlops-architecture-predictor-1  | INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
 ```

- Send a post request using the integration post request test.

 ```console
 python test/integration/predict_delivery_duration.py
 ```
- Alternativelly it is also posible to use the curl command.
 ```console
 curl -X POST http://localhost:8080/api/predict/delivery/duration -H 'Content-Type: application/json'  -d '{"id":12345,"delivery_person_age":30.0,"delivery_person_ratings":5.0,"restaurant_latitude":22.744648,"restaurant_longitude":75.894377,"delivery_location_latitude":22.824648,"delivery_location_longitude":75.974377,"weather_conditions":1,"road_traffic_density":3,"vehicle_condition":0,"type_of_order":3,"type_of_vehicle":2,"multiple_deliveries":0.0,"festival":1,"city":0,"city_code":10,"day":20,"month":3,"quarter":1,"year":2022,"day_of_week":6,"is_month_start":0,"is_month_end":0,"is_quarter_start":0,"is_quarter_end":0,"is_year_start":0,"is_year_end":0,"is_weekend":1,"order_prepare_time":15.0,"distance":12}'
 ```

- Verify the delivery duration prediction output.
 ```console
Response delivery duration service : {"duration_time":21.065946578979492}
Status code delivery duration service : 200
 ```
- Shut down the service.

 ```console
 docker compose down
 ```













