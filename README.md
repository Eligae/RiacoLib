## Rlib
for personal use(easier programming)

## to use

1. 시스템 환경 변수 편집 -> 환경변수 -> 시스템 변수 -> PYTHONPATH에 Rlib 지정
    ```bash
    C:\%your path to Rlib%\Rlib
    ```
2. cmd에서 확인
    ```bash
    echo %PYTHONPATH%
    
    >> C:\%your path to Rlib%\Rlib
    ```
3. 실제 사용 예시
    ```py
    from Rlib.Rmath import factorial
    print(factorial(5))

    >> 120
    ```
## files
|File|Actions|
|---|---|
|Rmath|for math, especially numeric|
|Rrequest|uses `request`. provide easier setting(headers are automatically setted)<br>Every action is trial and Error consequences, so it uses `Rerrorjson`|
|Rselenium|uses `selenium.webdriver`. same functions like `Rrequest`.|
|Rerrorjson|makes `Rerror.json` to keep track of all errors by doing large things.|