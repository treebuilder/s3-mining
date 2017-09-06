# s3-mining
Code to check AWS S3 buckets

Background:
•	Amazon AWS S3 buckets are used to store data (databases, files, etc.).
•	AWS S3 buckets can be misconfigured to be publicly accessible
•	AWS S3 buckets are trivially easy to search for
•	Insecure S3 buckets are becoming a more popular target for hackers, and breaches are making news (e.g., the story I circulated earlier today)

Testing for the existence of an S3 bucket is trivial:  Simply access https://s3.amazonaws.com/BUCKETNAME, and see what you get.
•	If it returns a 404, there’s no bucket by that name.
•	If it returns a 403, the bucket exists, but requires authentication to use
•	If it returns a 200, the bucket exists and is publicly accessible


Since this piqued my curiosity this morning, I whipped together some quick Python that will check a string to see whether it’s an S3 bucket and, if so, what its status is.
I tested it against the top 50 names in the Alexa Top 1 Million list (simply grabbed the leftmost label from the domain name and used that as the bucket name).

Spot #44 is xvideos.com.

Embarassingly, they have a public S3 bucket.

Installing the AWS CLI package (pip install awscli --upgrade --user), one can get a directory listing of it, copy files, upload files, delete, change, etc.

