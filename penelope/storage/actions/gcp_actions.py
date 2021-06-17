class FileActions:
    
    def upload_blob(bucket_id, source_file, destination_blob_name, client):
        """Uploads file to bucket"""
        # The ID of the bucket
        # The path of the file to upload
        # The destination of the uploaded file
        # A GCP storage client object

        bucket = client.bucket(bucket_id)
        blob = bucket.blob(destination_blob_name)
        
        blob.upload_from_filename(source_file)

        print(
            "File {} uploaded to {}.".format(
                source_file, destination_blob_name
            )
        )

    def download_blob(bucket_id, source_blob, destination_file, client):
        """Downloads file from bucket"""
        # The ID of the bucket
        # The path of the blob to download
        # The path of the downloaded file
        # A GCP storage client object

        bucket = client.bucket(bucket_id)
        blob = bucket.blob(source_blob)
        blob.download_to_filename(destination_file)

        print(
            "Blob {} download to {}.".format(
                source_blob, destination_file
            )
        )

    