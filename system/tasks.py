from zappa.asynchronous import task

@task
def changeEc2Instance(instance,newInstance):
  instance.stop()
  instance.wait_until_stopped()
  instance.modify_attribute(
      InstanceType={
          'Value': newInstance
      }
  )
  instance.start()
  instance.wait_until_running()

