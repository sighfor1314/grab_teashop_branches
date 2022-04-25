from branch import KebukeBranch
from actions import Actions

def main():
   environment = "qa"
   driver = Actions(environment)
   kebuke = KebukeBranch(driver)
   kebuke.kebukeBranch()


if __name__ == '__main__':
   main()

