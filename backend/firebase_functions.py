import firebase_admin
from firebase_admin import credentials, storage, firestore
from flask import request, redirect, url_for, render_template
from dotenv import load_dotenv
import os
from pdf_to_text import extract_pdf_text


# Initialize Firebase Admin SDK
load_dotenv()

cred_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
if not cred_path or not os.path.isfile(cred_path):
    raise ValueError(f"Invalid GOOGLE_APPLICATION_CREDENTIALS path: {cred_path}")

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {
    'storageBucket': 'freesic-storage.appspot.com'
})

# Initialize Firestore client
db = firestore.client()

latest_file = None

def upload_file():
    global latest_file

    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    if file:
        try:
            # Upload file to Firebase Storage
            bucket = storage.bucket()
            blob = bucket.blob(file.filename)
            blob.upload_from_file(file)

            # Save file metadata to Firestore
            doc_ref = db.collection('files').document()
            doc_ref.set({
                'filename': file.filename,
                'url': blob.public_url,
                'text_content': '',  # Placeholder for text content
                'id': doc_ref.id
            })

            # Update latest file
            latest_file = {
                'filename': file.filename,
                'url': blob.public_url,
                'text_content': '',  # Placeholder for text content
                'id': doc_ref.id
            }

            return redirect(url_for('manage'))
        except Exception as e:
            return f'Error: {str(e)}', 500

def manage_file():
    global latest_file

    files = [latest_file] if latest_file else []

    return render_template('manage.html', files=files)

def view_file(file_id):
    try:
        # Retrieve the specific document from Firestore
        doc_ref = db.collection('files').document(file_id)
        file = doc_ref.get().to_dict()

        if not file:
            return 'File not found', 404

        text_content = file.get('text_content', '')

        if not text_content:
            bucket = storage.bucket()
            blob = bucket.blob(file['filename'])
            text_content = extract_pdf_text(blob)
            file['text_content'] = text_content
            doc_ref.update({'text_content': text_content})

        return render_template('view.html', file=file)
    except Exception as e:
        return f'Error: {str(e)}', 500
