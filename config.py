import filters as f

INDIR = 'in'  # входная директория
OUTDIR = 'out'  # выходная директория

FILTER_LIST = [f.filter_alpha_keys, f.filter_available_values, f.filter_even_values]  # список фильтров.
# фильтры исполняются в том порядке, в каком записаны
