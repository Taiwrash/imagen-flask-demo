## Use this

On your Google cloud shell, run the following commands:

```bash
git clone https://github.com/Taiwrash/flask-imagen-demo.git
```

```bash
cd flask-imagen-demo
```
install the requirements

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

At this point you should be able to run both the frontend and backend on your local machine.

## Test the API

```bash
curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Create an image of a cartoon holding placard with \"google io abuja\""}' http://127.0.0.1:5000/api/generate
```


## Deployment

To deploy your Flask application with the HTML and CSS setup, you have several options depending on your needs and environment. Here’s a general guide for deploying a Flask app using some popular platforms:

### 1. **Deploy on Google Cloud Platform (GCP) using App Engine**

**Step 1: Install the Google Cloud SDK**

If you don’t have the Google Cloud SDK installed, download and install it from the [Google Cloud SDK website](https://cloud.google.com/sdk/docs/install).

**Step 2: Set Up Your Project**

```bash
gcloud init
```

Follow the prompts to set your project and configure your environment.

**Step 3: Create `app.yaml`**

In your project directory, create a file named `app.yaml` to define your App Engine configuration:

```yaml
runtime: python310

handlers:
- url: /static
  static_dir: static

- url: /.*
  script: auto
```

**Step 4: Deploy Your Application**

Make sure you are in the directory where your `app.py` and `requirements.txt` are located. Deploy using:

```bash
gcloud app deploy
```

**Step 5: Visit Your Deployed App**

```bash
gcloud app browse
```