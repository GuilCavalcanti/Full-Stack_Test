import { useState } from "react";
import { postRequest } from "../core/requests";

export function AssayForm({ data, refreshData }) {
  const [name, setName] = useState("");
  const [operator, setOperator] = useState(null);
  const [peptides, setPeptides] = useState("");
  const [error, setError] = useState("");

  const [assay_type, setAssay_type] = useState();
  const assayTypeOptions = ['Wet', 'Dry'];
  const assayTypeValues = ['WT', 'DY'];

  const save = (e) => {
    e.preventDefault();
    const peptidesList = peptides.split("\n");
    const payload = {
      name,
      operator,
      peptides: peptidesList,
      assay_type
    };
    postRequest("peptides/api/assays/", payload)
      .then(() => {
        setName("");
        setOperator(null);
        setPeptides("");
        refreshData();
      })
      .catch(() => {
        setError("Something went wrong!");
      });
  };

  /* Excercise 1 ADD-CODE-HERE */
  const userOptions = Object.values(data.users).filter((u) => u.groups_list.includes("Scientists")).map((s) => {
    return (
      <option value={s.id} key={s.id}>
        {s.full_name}
      </option>   
    );
  });

  return (
    <div className="assay-form">
      <h2>Add new assay</h2>
      {error && <div className="assay-form__error">{error}</div>}
      <form onSubmit={save}>
        <div className="assay-form__values">
          <Field label="Name">
            <input
              value={name}
              onChange={(e) => setName(e.target.value || "")}
            />
          </Field>
          <Field label="Operator">
            <select
              value={operator || ""}
              onChange={(e) => setOperator(e.target.value)}
            >
              <option />
              {userOptions}
            </select>
          </Field>
          <Field label="Assay Type">
            <select
              value={assay_type || ""}
              onChange={(e) => setAssay_type(e.target.value)}
            >
              <option />
              <option value={assayTypeValues[0]} key={assayTypeValues[0]}>
                {assayTypeOptions[0]}
              </option>
              <option value={assayTypeValues[1]} key={assayTypeValues[1]}>
                {assayTypeOptions[1]}
              </option>
            </select>
          </Field>
          <Field label="Peptides">
            <textarea
              value={peptides}
              onChange={(e) => setPeptides(e.target.value || "")}
            />
            <span style={{ fontSize: 10, color: "#888" }}>(one per line)</span>
          </Field>
        </div>
        <div className="assay-form__actions">
          <button className="assay-form__save" type="submit">
            Save
          </button>
        </div>
      </form>
    </div>
  );
}

function Field({ label, children }) {
  return (
    <div className="assay-form__field">
      <div className="assay-form__label">{label}</div>
      <div className="assay-form__control">{children}</div>
    </div>
  );
}
