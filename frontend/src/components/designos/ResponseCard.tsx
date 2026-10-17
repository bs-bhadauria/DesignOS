import { GenerateResponse } from "@/types/generate";

interface Props {
    response: GenerateResponse | null;
}

export default function ResponseCard({
    response,
}: Props) {

    if (!response) return null;

    return (

        <div className="rounded-xl border overflow-hidden">

            <div className="border-b px-6 py-4 flex justify-between items-center bg-slate-50">
                <div>
                    <h2 className="text-xl font-bold">
                        Deck Generated Successfully
                    </h2>

                    <p className="text-sm text-gray-500 mt-1">
                        Request ID : {response.request_id}
                    </p>
                </div>
                
                <a 
                    href="/preview" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-medium"
                >
                    Open Live Preview
                </a>
            </div>

        </div>

    );

}