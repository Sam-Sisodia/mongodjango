from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    contact = models.IntegerField()





class School(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE , related_name="school_student",null=True,blank=True)
    school_address = models.CharField(max_length=20)
    school_contact = models.IntegerField()


    def __str__(self):
        return self.name.name



'''

 const[students,setStudents]=useState([])


  useEffect(()=>{
    async function getAllStudent()
    {
      try{

        const students = await axios.get("http://127.0.0.1:8000/student/")
        console.log(students.data)
        setStudents(students.data)

      }
      catch(error){

      }
    }
    getAllStudent()

  },[])










  return (
    <div className="App">
      <h1>Conect React JS to Django </h1>

     
    </div>
  );
}

export default App;








'''