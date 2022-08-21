# Window에서 VIM 편집기 사용

### 1. vim Download
[다운로드](https://www.vim.org/download.php#pc) 에서 `gvim90.exe` 다운로드

### 2. Install
- 설치시 Create .bat files에 체크
  - 이렇게 설치하면 C:\WINDOWS에 vim.bat 파일이 생성됨
  - vi로 사용하고 싶은 경우 vim.bat 파일을 복사하여 vi.bat 생성
    - 관리자 권한으로 Powershell, cmd를 실행하여 다음 내용 입력
    ```shell
    copy C:\WINDOWS\vim.bat C:\WINDOWS\vi.bat
    ```

### 3. Customizing
- 설치시 기본 언어 한글
- 영어로 변경하고 싶다면 
  - (방법 1) C:\Program Files (x86)\Vim\vim90\lang 폴더 삭제
  - (방법 2) 관리자 권한으로 다음 내용 실행
  ```shell
  vi "C:\Program Files (x86)\Vim\_vimrc"
  ```
  파일의 첫 줄에 다음 내용 추가
  ```shell  
  language messages en
  ```



- [참고](https://meganad.github.io/2020-07-10-powershell-cmd-vi/)
