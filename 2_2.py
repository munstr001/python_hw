def check_winners(scores, student_score):
    if student_score in sorted(scores, reverse=True)[:3]:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")


if __name__ == "__main__":
    scores = list(map(int, input("Введите баллы участников через пробел: ").split()))
    student_score = int(input("Введите баллы Стаса: "))
    check_winners(scores, student_score)
