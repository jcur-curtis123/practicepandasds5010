from utils_package import utils
from plot_data import make_figure, make_line_plot, make_scatter_plot
from utils_package.utils import CWD


def main():

    '''
    gives user an option to choose which graph or plot to run

    read in via read_csv data/Wage.csv and define df
    '''
    df = utils.read_csv("data/Wage.csv")
    print("Pick a graph to run: ")
    print("1: Boxplot")
    print("2: Scatterplot")
    print("3: Lineplot")

    # choice for user validated via input 
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        make_figure(df)
    elif choice == "2":
        make_scatter_plot(df)
    elif choice == "3":
        make_line_plot(df)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

main()