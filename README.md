# content-management

### RUN
#### ```docker build -t content . && docker run -it -p 5000:5000 content```

### HOW TO USE?
#### Step 1
##### Upload article numbers: Send POST request to ```http://0.0.0.0:5000/api/send-primary-data/hamiltonwatch``` with file. You can view an example file in ```examples/hamiltonwatch1.csv```

#### Step 2
##### Save a response from the request in step 1 and edit it

#### Step 3
##### Upload file: send POST request to ```http://0.0.0.0:5000/api/send-new-file/hamiltonwatch``` with new file. You can view an example file in ```examples/hamiltonwatch2.csv```

#### Step 4
##### Publish data to site: send POST request to ```http://0.0.0.0:5000/api/publish/hamiltonwatch```