import jenkins.model.Jenkins
import org.jenkinsci.plugins.workflow.job.WorkflowJob
import org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition

def jenkins = Jenkins.get()
if (jenkins.getItem("delivery-monitoring") == null) {
    def job = jenkins.createProject(WorkflowJob, "delivery-monitoring")
    job.setDefinition(new CpsFlowDefinition(new File("/src/Jenkinsfile").text, true))
    job.save()
}
