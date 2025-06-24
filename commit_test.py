#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    print("안녕하세요! Git 커밋 테스트 파일입니다.")
    print("이 파일은 자동 커밋 및 푸시 테스트를 위해 생성되었습니다.")
    print("현재 시간:", __import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    # 간단한 계산 예시
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    print(f"숫자 리스트 {numbers}의 합계: {total}")
    
    print("테스트 완료!")

if __name__ == "__main__":
    main() 