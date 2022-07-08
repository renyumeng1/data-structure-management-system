select Tc.id, Tc.class_name, Tt.teacher_name
from Teachers_classes Tc
         join Teachers_teacher Tt on Tt.id = Tc.teacher_id;
