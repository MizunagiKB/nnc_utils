# -*- coding: utf-8 -*-
# ------------------------------------------------------------------ import(s)
import argparse
import sys
import os
import PIL.Image
import imagehash


# ------------------------------------------------------------------- param(s)
RESULT_FILENAME = "image_dc_result.tsv"


# ------------------------------------------------------------------- class(s)
# ----------------------------------------------------------------------------
class CImageProp(object):

    def __init__(self, image, hash_v, pathname):
        self.hash_v = hash_v
        self.pathname = pathname
        self.w = image.width
        self.h = image.height
        self.mode = image.mode
        self.format = image.format

    def __str__(self):
        return "%s\t%s\t%d\t%d\t%s\t%s" % (
            self.hash_v,
            self.pathname,
            self.w, self.h, self.mode, self.format
        )


# ---------------------------------------------------------------- function(s)
# ============================================================================
def proceed(src_dir, hash_function, hash_size, cb_log):

    dict_hash = {}

    for dir_name, _, list_filename in os.walk(src_dir):
        cb_log("checking ... %s" % dir_name)
        for filename in list_filename:
            if filename in (".DS_Store",):
                continue

            pathname = os.path.join(dir_name, filename)

            try:
                image = PIL.Image.open(pathname)
                hash_v = hash_function(image, hash_size)
            except OSError:
                continue

            o_prop = CImageProp(image, hash_v, pathname)

            if hash_v in dict_hash:
                dict_hash[hash_v].append(o_prop)
            else:
                dict_hash[hash_v] = [o_prop]

    n_dc_count = 0
    with open(RESULT_FILENAME, "w") as h:
        for hash_v, list_image in dict_hash.items():
            if len(list_image) > 1:
                n_dc_count += 1
                for o_prop in list_image:
                    text = "%s" % o_prop
                    cb_log(text)
                    h.write(text + "\n")
                cb_log("")

    if n_dc_count == 0:
        cb_log("No dupuliated.")
    else:
        cb_log("Found %d dupuliated." % n_dc_count)
        cb_log("Generate file > %s" % os.path.join(os.getcwd(), RESULT_FILENAME))


# ============================================================================
def cb_log(msg):
    print(msg)


# ============================================================================
def main():

    parser = argparse.ArgumentParser(description="Image duplication check")
    parser.add_argument(
        "-s", "--src", type=str, required=True,
                    help="Image check folder.")

    parser.add_argument(
        "-a", "--ahash", action="store_true", required=False, default=False,
                    help="use average hashing(aHash)")
    parser.add_argument(
        "-p", "--phash", action="store_true", required=False, default=False,
                    help="use perception hashing(pHash)")
    parser.add_argument(
        "-d", "--dhash", action="store_true", required=False, default=False,
                    help="use difference hashing(dHash)")
    parser.add_argument(
        "-w", "--whash", action="store_true", required=False, default=False,
                    help="use wavelet hashing(wHash)")

    o_argv = parser.parse_args()

    if o_argv.ahash is True:
        print("use ... average hashing")
        hash_function = imagehash.average_hash
    elif o_argv.phash is True:
        print("use ... perception hashing")
        hash_function = imagehash.phash
    elif o_argv.dhash is True:
        print("use ... difference hashing")
        hash_function = imagehash.dhash
    elif o_argv.whash is True:
        print("use ... wavelet hashing")
        hash_function = imagehash.whash
    else:
        print("use ... average hashing")
        hash_function = imagehash.average_hash

    proceed(o_argv.src_dir, hash_function, 8, default_log)


if __name__ == "__main__":
    main()



# [EOF]
