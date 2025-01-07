import sys
path = 'C:\Users\HP\Downloads\notenique'
if path not in sys.path:
    sys.path.insert(0, path)


from run import app

if __name__ == "__main__":
    app.run()
