import os

path_list = ["dokujo-tsushin", "it-life-hack", "kaden-channel"]

def get_sentence(path):
    f_list = os.listdir(path)
    s_list = []

    for lists in f_list:
        filePath = path + "/" + lists
        with open(filePath, encoding="utf-8_sig") as f:
            next(f)
            next(f)
            w = f.read().replace('\u3000', '').replace('\n', '')
            s_list.append(w)

    return s_list

def get_sentence_and_labels_for_training(base_path = "./text/"):
    s_list = []
    labels = []
    for p_list in path_list:
        path = base_path + p_list
        _s_list = get_sentence(path)

        s_list.extend(_s_list)

        for i in range(len(_s_list)):
            p_index = path_list.index(p_list)
            labels.append(p_index)

    return (s_list, labels)
