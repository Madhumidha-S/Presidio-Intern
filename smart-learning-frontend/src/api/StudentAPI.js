import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:3001/student",
  withCredentials: true,
});

export const fetchStudents = async ({ page = 1, search = "" }) => {
  const { data } = await API.get(`?page=${page}&search=${search}`);
  return data;
};

export const addStudent = async (student) => {
  const { data } = await API.post("/", student);
  return data;
};

export const updateStudent = async ({ id, ...student }) => {
  const { data } = await API.put(`/${id}`, student);
  return data;
};

export const deleteStudent = async (id) => {
  const { data } = await API.delete(`/${id}`);
  return data;
};
