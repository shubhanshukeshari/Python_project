pipeline {
	agent any
	stages {
		stage("Compile") {
			steps {
				echo "Python compile done"
			}
		}
		stage("Unit test") {
			steps {
				sh "python test_calc.py"
			}
		}
	}
}
