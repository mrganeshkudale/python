pipeline {
    agent any
    environment{
		IMAGE_NAME="localmachine/application:${BUILD_NUMBER}"
	}
    stages {
        stage('application-build') {
            steps {
		sh "cd /home/asawari/Code/sample-projects/demo/Python"
            }
	}
	stage('application-containerization'){
	    steps {
		sh "cd /home/asawari/Code/sample-projects/demo/Python && sudo -S docker build --build-arg DEPENDENCY=build/dependency -t local${BUILD_NUMBER} ."                
	    }
	}
	stage('image-versioning'){
	    steps {
		sh "sudo -S docker tag localpy${BUILD_NUMBER} localhost:5000/syntel/localpy${BUILD_NUMBER}"
		sh "sudo -S docker push localhost:5000/syntel/localpy${BUILD_NUMBER}"
	    }
	}
	stage('deploy-cloud'){
	    steps{
		sh "sudo -S kubectl create deployment localpydeployment${BUILD_NUMBER} --image=localhost:5000/syntel/localpy${BUILD_NUMBER}"
		sh "sudo -S kubectl expose deployment localpydeployment${BUILD_NUMBER} --type=LoadBalancer --port=8080 --name=localpyservice${BUILD_NUMBER}"
	    }
	}
    }
}

