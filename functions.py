def points(X: float, A: float, XAB_ratio: float, ABC_ratio: float, \
           BCD_ratio: float, XAD_ratio: float, ABCD_ratio: float) -> None:
    """Given the X point, A point, XAB ratio, ABC ratio, BCD ratio, XAD ratio,
    and AB=CD ratio, get the X point, A point, B point, C point, D point,
    XAD point, and ABCD point"""
    assert X > 0, "X must be greater than 0"
    assert A > 0, "A must be greater than 0"
    assert 0.382 <= XAB_ratio <= 3.618, "Ratios must be between 0.382 and 3.618"
    assert 0.382 <= ABC_ratio <= 3.618, "Ratios must be between 0.382 and 3.618"
    assert 0.382 <= BCD_ratio <= 3.618, "Ratios must be between 0.382 and 3.618"
    assert 0.382 <= XAD_ratio <= 3.618, "Ratios must be between 0.382 and 3.618"
    assert 0.382 <= ABCD_ratio <= 3.618, "Ratios must be between 0.382 and 3.618"
    B = A - ((A - X) * XAB_ratio)
    C = B - ((B - A) * ABC_ratio)
    D = C - ((C - B) * BCD_ratio)
    XAD = A - ((A - X) * XAD_ratio)
    ABCD = C - ((A - B) * ABCD_ratio)
    print(f"points: X={format(X, '.4f')}, A={format(A, '.4f')}, \
B={format(B, '.4f')}, C={format(C, '.4f')}, D={format(D, '.4f')}")
    print()
    print(f"potential reversal zone: D={format(D, '.4f')}, \
XAD={format(XAD, '.4f')}, ABCD={format(ABCD, '.4f')}")