$count = 10

1..$count | ForEach-Object -Parallel {python.exe E:\ILIM_stress\stress-master\multipple_test\start_test.py} -ThrottleLimit $count
