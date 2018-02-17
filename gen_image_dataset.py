# -*- coding: utf-8 -*-
# ------------------------------------------------------------------ import(s)
import sys
import os
import argparse
import csv
import hashlib
import random

import PIL.Image

W_SIZE = 28
H_SIZE = 28
SHUFFLE_COUNT = 10

# ============================================================================
def make_array(pathname, image_w, image_h):

    o_image = make_thumb(pathname, image_w, image_h)
    image_data = o_image.getdata()
    np_data = np.array(image_data)

    return np_data.reshape((3, image_w, image_h))

# ============================================================================
def make_thumb(pathname, image_w, image_h):

    o_image = PIL.Image.open(pathname)
    o_image.thumbnail((image_w, image_h))
    x_src, y_src = o_image.size
    o_thumb = PIL.Image.new("RGB", (image_w, image_h))

    x_pos = (image_w - x_src) >> 1
    y_pos = (image_h - y_src) >> 1

    o_thumb.paste(o_image, (x_pos, y_pos))

    return o_thumb

# ============================================================================
def make_image(src_pathname, dst_pathname, w=W_SIZE, h=H_SIZE):

    o_image_base = make_thumb(src_pathname, w, h)

    dst_dirname = os.path.split(dst_pathname)[0]

    dst_filename = hashlib.sha1(dst_pathname.encode("utf-8")).hexdigest() + ".png"

    if os.path.exists(dst_dirname) is not True:
        os.mkdir(dst_dirname)

    o_image_base.save(
        os.path.join(dst_dirname, dst_filename)
    )

    return dst_dirname, dst_filename

# ============================================================================
def recursive_split_path(dirname):

    head_dir, tail_dir = os.path.split(dirname)
    if len(head_dir) > 0:
        return recursive_split_path(head_dir) + [tail_dir]
    else:
        return [tail_dir]


# ============================================================================
def generate_csv(dict_dir, o_argv, export_dir, csv_filename, dict_class):

    class_size = len(dict_class)
    import_dir = o_argv.src

    list_record = []
    for class_name, list_filename in dict_dir.items():
        for filename in list_filename:
            dst_dirname, dst_filename = make_image(
                os.path.join(import_dir, class_name, filename),
                os.path.join(export_dir, class_name, filename),
                o_argv.x_size,
                o_argv.y_size
            )

            list_record.append(
                ["/".join([".", class_name, dst_filename])] + dict_class[class_name]
            )

    for _ in range(10):
        random.shuffle(list_record)

    with open(os.path.join(export_dir, csv_filename), "w") as h_writer:
        o_writer = csv.writer(h_writer, lineterminator="\n")
        o_writer.writerow(["x", "y_index"] + ["y_class__%d" % n for n in range(class_size)])
        for r in list_record:
            o_writer.writerow(r)

    print("export csv ... %s(%4d)" % (os.path.join(export_dir, csv_filename), len(list_record)))


# ============================================================================
def random_pickup(list_filename, gen_size):

    assert(gen_size >= len(list_filename))

    list_gen_filename = []

    if len(list_filename) > 0:
        pickup_count = gen_size - len(list_filename)

        for _ in range(pickup_count):
            list_temp = list_filename[:]
            random.shuffle(list_temp)

            list_gen_filename.append(list_temp[0])

    return list_gen_filename


# ============================================================================
def main():

    parser = argparse.ArgumentParser(description="Train CSV Generator for NNC")
    parser.add_argument(
        "-s", "--src", type=str, required=True,
                    help="source folder.")
    parser.add_argument(
        "-d", "--dst", type=str, required=True,
                    help="destination folder.")
    parser.add_argument(
        "-i", "--ignore", type=str, required=False, default="",
                    help="ignore folder.")
    parser.add_argument(
        "-v", "--valid", type=str, required=False,
                    help="validation folder.")
    parser.add_argument(
        "-e", "--even", action="store_true", required=False, default=False,
                    help="Even Train data(s)")
    parser.add_argument(
        "-f", "--full", action="store_true", required=False, default=False,
                    help="Full Train data(s)")
    parser.add_argument(
        "-x", "--x-size", type=int, required=False, default=W_SIZE,
                    help="image x size(width)")
    parser.add_argument(
        "-y", "--y-size", type=int, required=False, default=H_SIZE,
                    help="image y size(height)")
    parser.add_argument(
        "-r", "--ratio", type=float, required=False,
                    help="validation data ratio")

    o_argv = parser.parse_args()

    exist_dir = [o_argv.src, o_argv.dst]

    if o_argv.valid is not None:
        if o_argv.ratio is None:
            parser.print_help()
            sys.exit()
        if o_argv.ratio >= 1.0 or o_argv.ratio < 0.0:
            parser.print_help()
            sys.exit()
        exist_dir.append(o_argv.valid)

    if all(exist_dir) is not True:
        parser.print_help()
        sys.exit()

    #print o_argv
    #sys.exit()

    src_base = os.path.split(o_argv.src)[-1]
    print("src_base    < %s" % src_base)
    dst_base = os.path.split(o_argv.dst)[-1]
    print("dst_base    > %s" % dst_base)

    if o_argv.valid is not None:
        valid_base = os.path.split(o_argv.valid)[-1]
        print("valid_base  > %s" % valid_base)

    print("image width : %4d" % o_argv.x_size)
    print("image height: %4d" % o_argv.y_size)

    dict_dir_s = {}
    dict_dir_w = {}

    base_dir_level = len(recursive_split_path(o_argv.src))
    for dirname, _, list_filename in os.walk(o_argv.src):
        if len(list_filename) == 0:
            continue

        list_subdirname = recursive_split_path(dirname)
        if len(list_subdirname) != base_dir_level + 1:
            continue

        class_name = list_subdirname[-1]

        if class_name == o_argv.ignore:
            continue

        list_suffle = [f for f in list_filename if f[0] not in (".",)]
        random.shuffle(list_suffle)
        dict_dir_w[class_name] = list_suffle

    if o_argv.even is True:
        min_size = min([len(r) for r in dict_dir_w.values()])

        print("enable even : record size(%4d)" % min_size)

        for class_name, list_filename in dict_dir_w.items():
            dict_dir_s[class_name] = list_filename[0:min_size]

    elif o_argv.full is True:
        max_size = max([len(r) for r in dict_dir_w.values()])

        print("enable full : record size(%4d)" % max_size)

        for class_name, list_filename in dict_dir_w.items():
            dict_dir_s[class_name] = list_filename + random_pickup(list_filename, max_size)

    else:
        for class_name, list_filename in dict_dir_w.items():
            dict_dir_s[class_name] = list_filename[:]

    dict_dir_d = {}
    dict_dir_v = {}

    for class_name, list_filename in dict_dir_s.items():
        if o_argv.valid is None:
            dict_dir_d[class_name] = list_filename
        else:
            list_shuffle = list_filename[:]
            random.shuffle(list_shuffle)
            item_count = len(list_shuffle)
            item_ratio = int(item_count * o_argv.ratio)
            dict_dir_d[class_name] = list_shuffle[0:item_count - item_ratio]
            dict_dir_v[class_name] = list_shuffle[item_count - item_ratio:]
            print("ratio %16s(%4d) ... %4d:%4d" % (class_name, item_count, item_count - item_ratio, item_ratio))

    class_size = len(dict_dir_s.keys())

    dict_class = {}
    for n, class_name in enumerate(dict_dir_s.keys()):
        list_hv = [0.0] * class_size
        list_hv[n] = 1.0
        dict_class[class_name] = [n] + list_hv

    generate_csv(dict_dir_d, o_argv, o_argv.dst, dst_base + ".csv", dict_class)
    if o_argv.valid is not None:
        generate_csv(dict_dir_v, o_argv, o_argv.valid, valid_base + ".csv", dict_class)


if __name__ == "__main__":
    main()



# [EOF]
