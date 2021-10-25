pipeline {
	agent any
	triggers {
        pollSCM('* * * * *') //runs this pipeline on every commit
        cron('19 53 * * *') //run at 23:30:00 
    }
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
