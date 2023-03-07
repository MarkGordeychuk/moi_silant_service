import React from "react";
import { Link } from "react-router-dom";

import styles from "../styles/Table.module.sass";


export interface TableProps<T> {
    columns: string[],
    keys: string[],
    directoryKeys: Set<string>,
    uniqueKey: string,
    data: T[],
    children?: React.ReactNode,
    editable?: boolean,
    editLink?: string,
}

function Table<T>({data, columns, keys, directoryKeys, uniqueKey, children, ...edit}: TableProps<T>) {
    edit = { editable: true, editLink: '/' }

    return (<div className={styles.container}>
        { children || null }
        <table className={styles.table}>
            <thead>
                <tr>
                    { columns.map(column => (<td key={column}>{column}</td>)) }
                </tr>
            </thead>
            <tbody>
                { data.map((element) => (
                    <tr key={element[uniqueKey]}>
                        { keys.map((key) => (
                            <td key={element[uniqueKey] + key}>
                                { directoryKeys.has(key)
                                    ? <Link to={`/directory/${element[key].id}/`}>{element[key].name}</Link>
                                    : element[key] }
                            </td>
                        ))}
                        {
                            edit.editable ? <td>
                                <Link to={ edit.editLink.replace("<pk>", element[uniqueKey]) }>Edit</Link>
                            </td> : null
                        }
                    </tr>
                ))}
            </tbody>
        </table>
    </div>)
}

export default Table;