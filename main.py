import config
import os
import json

from filters import FilterError


def filtered(key, value):
    """
    Применение фильтров к записи, формат совпадает с форматом фильтров
    """
    status, tmpkey, tmpval = True, key, value
    try:
        for filterfunc in config.FILTER_LIST:
            status, (tmpkey, tmpval) = filterfunc(tmpkey, tmpval)
            if not status:
                return status, (tmpkey, tmpval)
    except Exception as E:
        raise FilterError("An error occurred while using filter:", filterfunc, "\nException: ", E)
    return status, (tmpkey, tmpval)


filenames = os.listdir(config.INDIR)

for file in filenames:
    try:
        fp_in = open(os.path.join(config.INDIR, file), "r")
        json_in = json.load(fp_in)
        fp_in.close()
        if isinstance(json_in, dict):
            result = dict()
            for key, value in json_in.items():
                status, (tmpkey, tmpval) = filtered(key, value)
                if status:
                    result[tmpkey] = tmpval
            if os.path.isfile(os.path.join(config.OUTDIR, file)):
                fp_out = open(os.path.join(config.OUTDIR, file), "w")
            else:
                fp_out = open(os.path.join(config.OUTDIR, file), "x")
            json.dump(result, fp_out)
            fp_out.close()
        else:
            raise AssertionError("Wrong file format in ", file)
    except AssertionError as AE:
        print(AE)
    except RuntimeError as RE:
        print(RE)
        exit(0)
