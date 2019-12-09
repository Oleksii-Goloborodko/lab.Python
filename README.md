# requirements

- llvm
- gcc, mingw

# compile

- Create and activate virtualenv
- pip install -r requirements.txt

```bash
python main.py
llc output.ll
gcc -c output.s -o output.o 
gcc output.o -o output -no-pie
./output
```

