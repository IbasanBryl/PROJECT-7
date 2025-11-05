import traceback
from gui import AttendanceGUI

def main():
    """Main function to run the application."""
    try:
        app = AttendanceGUI()
        app.run()
    except Exception as e:
        print(f"Application error: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()