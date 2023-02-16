from inline import Here

    
sample = "Hello"
size_string = 32
doubled = sample.zfill(size_string)
Here().given(sample, "test_G").given(size_string, 15).check_eq(doubled, "000000000test_G")