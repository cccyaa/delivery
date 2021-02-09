# delivery

1. Setting up this application on Google Cloud:

   ~~~bash
   git clone https://github.com/cccyaa/delivery.git
   cd delivery
   ~~~

2. create a virtual environment and source it

   ~~~bash
   python3 -m venv ~/.delivery
   source ~/.delivery/bin/activate
   ~~~

3. install dependencies and run at local environment

   ~~~bash
   make install
   python main.py
   ~~~

4. run at a public url

   ~~~bash
   gcloud app create
   gcloud app deploy
   ~~~

5. do as the tutorial says: https://cloud.google.com/source-repositories/docs/quickstart-triggering-builds-with-source-repositories

6. push a change and view the cloud view history at  https://console.cloud.google.com/cloud-build/builds?project=delivery-303413
