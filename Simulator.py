from Utility.Inputs import InputTaker

from GraphPlot import Plotter
from Model import LorenzModel
from PredictabilityHorizons import PredictabilityHorizon

PreDefMap = dict({
    1: [10, 8/3, 28],
    2: [10, 8/3, 99.65],
    3: [10, 8/3, 15],
    4: [10, 8/3, 166.072],
})

BehaviorMap = {1: "Chaotic Convections", 2: "Torus Knot (Periodic)", 3: "Stable Point", 4: "Chaotic Bursts"}

class Simulator:
    
    def __init__(self):
        self.model1 = None
        self.model2 = None


    def _printSavedModels(self):
        if self.model1 is None and self.model2 is None:
            return
        print("\n---------------CURRENTLY SAVED MODELS---------------\n")
        if self.model1 is not None:
            print(f"1. {self.model1.behavior}")
        if self.model2 is not None:
            print(f"2. {self.model2.behavior}")


    def _createModelFromSelection(self, menuTitle=""):
        constants, initial, behav = self.selectAnimationParams(menuTitle)
        if constants is None or initial is None or behav is None:
            return None
        return LorenzModel(constants, initial, behav)


    def _replaceModel(self, slot):
        new_model = self._createModelFromSelection(
            "\n---------- REPLACE MODEL {} ----------\n".format(slot)
        )
        if new_model is None:
            return None
        if slot == 1:
            self.model1 = new_model
        else:
            self.model2 = new_model
        return new_model
    
    
    def runAnimateOneMenu(self):
        while True:
            print("\n-----------------ANIMATE LORENZ (ONE)--------------------\n")
            self._printSavedModels()

            if self.model1 is not None and self.model2 is not None:
                print("\nChoose a model:")
                print("1. Use saved model 1")
                print("2. Use saved model 2")
                print("3. Replace one model and use it")
                choice = InputTaker.readInt("> ", range(1, 4))
                if choice is None:
                    return

                if choice == 1:
                    Plotter.plotSingle(self.model1)
                    return
                if choice == 2:
                    Plotter.plotSingle(self.model2)
                    return

                slot = InputTaker.readInt("Replace which model? (1/2): ", range(1, 3))
                if slot is None:
                    return
                model = self._replaceModel(slot)
                if model is None:
                    continue
                Plotter.plotSingle(model)
                return

            if self.model1 is not None and self.model2 is None:
                print("\nChoose a model:")
                print("1. Use saved model 1")
                print("2. Replace saved model 1")
                print("3. Create saved model 2 and use it")
                choice = InputTaker.readInt("> ", range(1, 4))
                if choice is None:
                    return
                if choice == 1:
                    Plotter.plotSingle(self.model1)
                    return
                if choice == 2:
                    model = self._replaceModel(1)
                    if model is None:
                        continue
                    Plotter.plotSingle(model)
                    return

                model = self._replaceModel(2)
                if model is None:
                    continue
                Plotter.plotSingle(model)
                return

            if self.model1 is None and self.model2 is not None:
                print("\nChoose a model:")
                print("1. Use saved model 2")
                print("2. Replace saved model 2")
                print("3. Create saved model 1 and use it")
                choice = InputTaker.readInt("> ", range(1, 4))
                if choice is None:
                    return
                if choice == 1:
                    Plotter.plotSingle(self.model2)
                    return
                if choice == 2:
                    model = self._replaceModel(2)
                    if model is None:
                        continue
                    Plotter.plotSingle(model)
                    return

                model = self._replaceModel(1)
                if model is None:
                    continue
                Plotter.plotSingle(model)
                return

            # No saved models yet: create model 1 by default.
            model = self._replaceModel(1)
            if model is None:
                continue
            Plotter.plotSingle(model)
            return
            
            
    def predefinedValues(self):
        print("\n---------- PRE-DEFINED VALUES -------------\n")
        print("1. Atmospheric Heat Convections (Chaotic)")
        print("2. The Torus Knot (Periodic)")
        print("3. The Stable Point (Stabilizes)")
        print("4. Intermittency (Chaotic Bursts)")

        behav = InputTaker.readInt("> ", range(1, 5))
        if behav is None:
            return None, None, None

        return PreDefMap[behav], [1, 1, 1], BehaviorMap[behav]


    def customValues(self):
        print("\n----------CUSTOM VALUES--------------\n")
        print("Enter values in appropriate ranges for best experience:")

        sigma = InputTaker.readFloat("sigma (Range 0-20): ")
        beta = InputTaker.readFloat("beta (range 0-10): ")
        rho = InputTaker.readFloat("rho (range 0-100+): ")

        if sigma is None or beta is None or rho is None:
            print("Invalid numeric input. Falling back to defaults.")
            return [10, 8 / 3, 28], [1, 1, 1], "Default Sigma: 10, Beta: 8/3, Rho: 28"

        print("Use predefined initial values for variables? (Y/N)")
        predefInit = input("> ").strip().upper()

        if not InputTaker.validifyRange(predefInit, ["Y", "N"]) or predefInit == "Y":
            initial = [1, 1, 1]
        else:
            raw = input("Enter X Y Z (Space-Separated): ").strip().split()
            try:
                initial = list(map(float, raw))
            except ValueError:
                initial = [1, 1, 1]

            if len(initial) != 3:
                initial = [1, 1, 1]

        return [sigma, beta, rho], initial, f"Custom Sigma: {sigma}, Beta: {beta}, Rho: {rho}"


    def selectAnimationParams(self, menuTitle=""):
        while True:
            if menuTitle:
                print(menuTitle)
            print("1. Pre-defined values for different attractor behaviors")
            print("2. Custom values")
            print("3. Back")
            choice = InputTaker.readInt("> ", range(1, 4))
            if choice is None:
                continue

            if choice == 3:
                return None, None, None

            if choice == 1:
                constants, initial, behav = self.predefinedValues()
            else:
                constants, initial, behav = self.customValues()

            if constants is None or initial is None:
                continue

            return constants, initial, behav




    def runAnimateTwoMenu(self):
        while True:
            print("\n-----------------ANIMATE LORENZ (TWO)--------------------\n")
            self._printSavedModels()

            if self.model1 is not None and self.model2 is not None:
                print("\nChoose models:")
                print("1. Use saved models (1 & 2)")
                print("2. Replace model 1 and animate")
                print("3. Replace model 2 and animate")
                print("4. Replace both models and animate")
                choice = InputTaker.readInt("> ", range(1, 5))
                if choice is None:
                    return

                if choice == 2:
                    if self._replaceModel(1) is None:
                        continue
                elif choice == 3:
                    if self._replaceModel(2) is None:
                        continue
                elif choice == 4:
                    if self._replaceModel(1) is None:
                        continue
                    if self._replaceModel(2) is None:
                        continue

                Plotter.plotDouble(self.model1, self.model2)
                return

            # Ensure both models exist.
            if self.model1 is None:
                if self._replaceModel(1) is None:
                    continue
            if self.model2 is None:
                if self._replaceModel(2) is None:
                    continue

            Plotter.plotDouble(self.model1, self.model2)
            return


    def runAnimateMenu(self):
        while True:
            print("\n-----------------ANIMATE LORENZ--------------------\n")
            print("1. Animate one Lorenz model")
            print("2. Animate two Lorenz models")
            print("3. Back")
            num_models = InputTaker.readInt("> ", range(1, 4))
            if num_models is None:
                continue

            if num_models == 3:
                return
            if num_models == 1:
                self.runAnimateOneMenu()
            else:
                self.runAnimateTwoMenu()


    def _runCorrelations(self, model_a, model_b):
        PredictabilityHorizon(model_a, model_b).runCorrelationsPlot()


    def horizonsPredefined(self):
        while True:
            print("\n---------- PRE-DEFINED HORIZONS -------------\n")
            print("1. Pair 1: Stable/steady vs chaotic")
            print("2. Pair 2: Near-transition vs fully chaotic")
            print("3. Back")

            choice = InputTaker.readInt("> ", range(1, 4))
            if choice is None:
                continue

            if choice == 3:
                return

            # Model expects constants in (sigma, beta, rho) order.
            initial = [1, 1, 1]

            if choice == 1:
                # A (steady): (sigma, rho, beta) = (10, 10, 8/3)
                # B (chaotic): (10, 28, 8/3)
                model_a = LorenzModel([10, 8 / 3, 10], initial, "Horizon A: steady")
                model_b = LorenzModel([10, 8 / 3, 28], initial, "Horizon B: chaotic")
            else:
                # A (near transition): (10, 24.0, 8/3)
                # B (classic chaos): (10, 28, 8/3)
                model_a = LorenzModel([10, 8 / 3, 24.0], initial, "Horizon A: near-transition")
                model_b = LorenzModel([10, 8 / 3, 28], initial, "Horizon B: chaotic")

            return model_a, model_b


    def horizonsCustom(self):
        print("\n---------- CUSTOM HORIZONS -------------\n")
        print("Enter coefficients for system A (sigma, beta, rho)")
        sigma_a = InputTaker.readFloat("A sigma: ")
        beta_a = InputTaker.readFloat("A beta: ")
        rho_a = InputTaker.readFloat("A rho: ")

        print("\nEnter coefficients for system B (sigma, beta, rho)")
        sigma_b = InputTaker.readFloat("B sigma: ")
        beta_b = InputTaker.readFloat("B beta: ")
        rho_b = InputTaker.readFloat("B rho: ")

        if (
            sigma_a is None
            or beta_a is None
            or rho_a is None
            or sigma_b is None
            or beta_b is None
            or rho_b is None
        ):
            print("Invalid numeric input. Please try again.")
            return

        initial = [1, 1, 1]
        model_a = LorenzModel([sigma_a, beta_a, rho_a], initial, "Horizon A (custom)")
        model_b = LorenzModel([sigma_b, beta_b, rho_b], initial, "Horizon B (custom)")
        return model_a, model_b

    def runPredictabilityHorizonsMenu(self):
        while True:
            print("\n------------PREDICTABILITY HORIZONS-------------\n")
            self._printSavedModels()

            if self.model1 is not None and self.model2 is not None:
                print("\n\n1. Use saved models (1 & 2)")
                print("2. Replace saved models with pre-defined inputs")
                print("3. Replace saved models with custom inputs")
                print("4. Back")
                choice = InputTaker.readInt("> ", range(1, 5))
                if choice is None:
                    return
                if choice == 4:
                    return
                if choice == 1:
                    self._runCorrelations(self.model1, self.model2)
                    return
                if choice == 2:
                    built = self.horizonsPredefined()
                    if built is None:
                        continue
                    (self.model1, self.model2) = built
                    self._runCorrelations(self.model1, self.model2)
                    return
                if choice == 3:
                    built = self.horizonsCustom()
                    if built is None:
                        continue
                    (self.model1, self.model2) = built
                    self._runCorrelations(self.model1, self.model2)
                    return

            print("1. Plot predictability horizons (pre-defined inputs)")
            print("2. Plot predictability horizons (custom inputs)")
            print("3. Back")
            choice = InputTaker.readInt("> ", range(1, 4))
            if choice is None:
                continue
            if choice == 3:
                return
            if choice == 1:
                built = self.horizonsPredefined()
            else:
                built = self.horizonsCustom()
            if built is None:
                continue
            (self.model1, self.model2) = built
            self._runCorrelations(self.model1, self.model2)
            return


    def runFeatureMenu(self):
        while True:
            print("\n-----------------MAIN MENU--------------------\n")
            print("1. Animate Lorenz attractor")
            print("2. Plot predictability horizons")
            print("3. Exit")
            choice = InputTaker.readInt("> ", range(1, 4))
            if choice is None:
                continue

            if choice == 1:
                self.runAnimateMenu()
            elif choice == 2:
                self.runPredictabilityHorizonsMenu()
            else:
                return


if (__name__ == "__main__"):
    sim = Simulator()
    sim.runFeatureMenu()
