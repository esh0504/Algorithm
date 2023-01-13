def main():
    w, h, f, c, x1, y1, x2, y2 = map(int, input().split())
    make_x_len = w - f
    if make_x_len < w // 2:
        make_x_len = w - make_x_len
    split_y = c + 1
    total_ = w * h
    split_x = w - make_x_len
    n = x2 - x1
    if x1 < split_x:
        if x2 > split_x:
            n += (split_x - x1)
        else:
            n *= 2
    print(total_ - (n * (y2 - y1) * split_y))

main()