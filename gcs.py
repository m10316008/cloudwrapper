"""Google Cloud Storage using GCE Authentication."""

import os

from time import sleep
from gcloud import storage
from gcloud.exceptions import GCloudError


class GcsConnection(object):

    def __init__(self):
        self.connection = storage.Client()

    def bucket(self, name):
        for _ in range(6):
            try:
                return Bucket(self.connection.get_bucket(name))
            except IOError as e:
                if e.errno == errno.EPIPE:
                    self.connection = storage.Client()
                sleep(10)
            except GCloudError:
                sleep(30)



class Bucket(object):

    def __init__(self, handle):
        self.handle = handle

    def put(self, source, target):
        key = self.handle.blob(target)
        key.upload_from_filename(source)
        # multipart = self.handle.initiate_multipart_upload(target)
        # try:
        #     with open(source, 'rb') as fp:
        #         offsets = xrange(0, source_size, self.PART_LIMIT)
        #         for part, offset in enumerate(offsets, start=1):
        #             size = min(source_size, offset + self.PART_LIMIT) - offset
        #             fp.seek(offset)
        #             multipart.upload_part_from_file(fp, part, size=size)
        #     multipart.complete_upload()
        # except:
        #     multipart.cancel_upload()
        #     raise

    def get(self, source, target):
        key = self.handle.get_blob(source)
        key.download_to_filename(target)

    def has(self, source):
        key = self.handle.blob(source)
        return key.exists()