# Ditionary


print('Data ini dikirimkan oleh server gojek, untuk memberikan info driver terdekat di sekitar user')

data_gojek = {
    'tanggal': '2020-07-27',
    'driver_list': [{'nama': 'satu', 'jarak': 10}, {'nama': 'dua', 'jarak': 50}, {'nama': 'tiga', 'jarak': 100},
                    {'nama': 'empat', 'jarak': 1000}]
}
print(data_gojek)
print(f"driver disekitar sini {data_gojek['driver_list']}")
print(f"driver #1 {data_gojek['driver_list'][0]}")
print(f"jarak driver #1 {data_gojek['driver_list'][0]['jarak']}meter" )