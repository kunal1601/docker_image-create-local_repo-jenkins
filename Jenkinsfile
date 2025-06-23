  pipeline {
  agent {
        label "agent1"
    } 
    environment {
        JAVA_HOME = "/usr/lib/jvm/java-21-amazon-corretto.x86_64"
        PATH = "${JAVA_HOME}/bin:${env.PATH}"
       }
       stages{
       stage('SCM') {
               steps {
                   git 'https://github.com/kunal1601/docker_image-create-local_repo-jenkins.git'
               }
           }
       stage('docker image creation'){
           steps{
               sh 'sudo docker build -t kunal0816/docker-web_app:v${BUILD_NUMBER} .'
               sh 'sudo docker tag kunal0816/docker-web_app:v${BUILD_NUMBER} localhost:5000/docker-web_app:v${BUILD_NUMBER}'

           }
       }
        stage('Docker Local_Registry') {
         steps {
            sh 'sudo docker rm -f registry'
            sh 'sudo docker run -d -p 5000:5000 --name registry registry:2'
            sh 'sudo docker push localhost:5000/docker-web_app:v${BUILD_NUMBER}'
        }
     } 
     stage('Production Env') {
         steps {
             sshagent(['QA_env_id']) {
              sh """
                ssh -o StrictHostKeyChecking=no ec2-user@13.203.101.95 <<EOF
                sudo yum install docker -y
                sudo systemctl stop docker
                sudo echo '{ "insecure-registries":["172.31.1.249:5000"] }' | sudo tee /etc/docker/daemon.json
                sudo systemctl daemon-reexec
                sudo systemctl start docker
                sudo systemctl enable docker
                
                sudo docker rm -f web_app || true
                sudo docker run -d --name web_app -p 5000:5000 172.31.1.249:5000/docker-web_app:v${BUILD_NUMBER}
EOF
            """
         }
     }
   } 
 }
}
